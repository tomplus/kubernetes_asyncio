#!/bin/bash

# Copyright 2015 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Script to fetch latest swagger spec.
# Puts the updated spec at api/swagger-spec/

set -o errexit
set -o nounset
set -o pipefail

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
CLIENT_ROOT="$(dirname ${SCRIPT_ROOT})/kubernetes_asyncio"
CLIENT_VERSION=$(python "${SCRIPT_ROOT}/constants.py" CLIENT_VERSION)
PACKAGE_NAME=$(python "${SCRIPT_ROOT}/constants.py" PACKAGE_NAME)
DEVELOPMENT_STATUS=$(python "${SCRIPT_ROOT}/constants.py" DEVELOPMENT_STATUS)

pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

pushd "${CLIENT_ROOT}" > /dev/null
CLIENT_ROOT=`pwd`
popd > /dev/null

TEMP_FOLDER=$(mktemp -d) 
trap "rm -rf ${TEMP_FOLDER}" EXIT SIGINT

SETTING_FILE="${TEMP_FOLDER}/settings"
echo "export KUBERNETES_BRANCH=\"$(python ${SCRIPT_ROOT}/constants.py KUBERNETES_BRANCH)\"" > $SETTING_FILE
echo "export CLIENT_VERSION=\"$(python ${SCRIPT_ROOT}/constants.py CLIENT_VERSION)\"" >> $SETTING_FILE
echo "export PACKAGE_NAME=\"client\"" >> $SETTING_FILE
# openapi-generator v5.4.0
echo "export OPENAPI_GENERATOR_COMMIT=4a36be70025e9c0d3ff61731618b7fc2d942c4b6" >> $SETTING_FILE
echo "unset USERNAME" >> $SETTING_FILE

if [[ -z ${GEN_ROOT:-} ]]; then
    GEN_ROOT="${TEMP_FOLDER}/gen"
    echo ">>> Cloning gen repo"
    git clone --recursive https://github.com/kubernetes-client/gen.git "${GEN_ROOT}"
else
    echo ">>> Reusing gen repo at ${GEN_ROOT}"
fi

echo ">>> Running python generator from the gen repo"
"${GEN_ROOT}/openapi/python-asyncio.sh" "${CLIENT_ROOT}" "${SETTING_FILE}"
mv "${CLIENT_ROOT}/swagger.json" "${SCRIPT_ROOT}/swagger.json"

echo ">>> updating version information..."
sed -i'' "s/^CLIENT_VERSION = .*/CLIENT_VERSION = \\\"${CLIENT_VERSION}\\\"/" "${SCRIPT_ROOT}/../setup.py"
sed -i'' "s/^__version__ = .*/__version__ = \\\"${CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"
sed -i'' "s/^PACKAGE_NAME = .*/PACKAGE_NAME = \\\"${PACKAGE_NAME}\\\"/" "${SCRIPT_ROOT}/../setup.py"
sed -i'' "s,^DEVELOPMENT_STATUS = .*,DEVELOPMENT_STATUS = \\\"${DEVELOPMENT_STATUS}\\\"," "${SCRIPT_ROOT}/../setup.py"

echo ">>> fix generated rest client for patching with strategic merge..."
patch "${CLIENT_ROOT}/client/rest.py" "${SCRIPT_ROOT}/rest_client_patch.diff"
echo ">>> fix generated rest client by increasing aiohttp read buffer to 2MiB..."
patch "${CLIENT_ROOT}/client/rest.py" "${SCRIPT_ROOT}/rest_client_patch_read_bufsize.diff"
echo ">>> fix generated rest client to support customer server hostname TLS verification..."
patch "${CLIENT_ROOT}/client/rest.py" "${SCRIPT_ROOT}/rest_client_server_hostname_patch.diff"


echo ">>> Remove invalid tests (workaround https://github.com/OpenAPITools/openapi-generator/issues/5377)"
grep -r make_instance "${CLIENT_ROOT}/test/" | awk '{ gsub(":", ""); print $1}' | sort | uniq | xargs rm

echo ">>> Done."
