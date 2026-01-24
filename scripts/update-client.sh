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
sed -i'' "s/^version = .*/version = \\\"${CLIENT_VERSION}\\\"/" "${SCRIPT_ROOT}/../pyproject.toml"
sed -i'' "s/^__version__ = .*/__version__ = \\\"${CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"

echo ">>> copy patched files"
cp -b "${SCRIPT_ROOT}/patched_files/api_client.py" "${CLIENT_ROOT}/client/api_client.py"
cp -b "${SCRIPT_ROOT}/patched_files/rest.py" "${CLIENT_ROOT}/client/rest.py"
cp -b "${SCRIPT_ROOT}/patched_files/configuration.py" "${CLIENT_ROOT}/client/configuration.py"

echo ">>> don't deep-copy configuration for local_vars_configuration in models"
find "${CLIENT_ROOT}/client/models/" -type f -print0 | xargs -0 sed -i 's/local_vars_configuration = Configuration.get_default_copy()/local_vars_configuration = Configuration.get_default()/g'

echo ">>> Remove invalid tests (workaround https://github.com/OpenAPITools/openapi-generator/issues/5377)"
grep -r make_instance "${CLIENT_ROOT}/test/" | awk '{ gsub(":", ""); print $1}' | sort | uniq | xargs rm

echo ">>> Fix API tests (https://github.com/aio-libs/aiohttp/issues/8555)"
find "${CLIENT_ROOT}/test/" -type f -print0 | xargs -0 sed -i -e 's/unittest.TestCase/unittest.IsolatedAsyncioTestCase/g' -e 's/def setUp(self):/async def asyncSetUp(self):/g'

echo ">>> add type stub files for generated files"
PYTHONPATH="$(dirname ${SCRIPT_ROOT})" python "${SCRIPT_ROOT}/generate_typing.py"

echo ">>> add __all__ for generated files"
PYTHONPATH="$(dirname ${SCRIPT_ROOT})" python "${SCRIPT_ROOT}/add__all__.py" "${CLIENT_ROOT}/client/models/__init__.py"
PYTHONPATH="$(dirname ${SCRIPT_ROOT})" python "${SCRIPT_ROOT}/add__all__.py" "${CLIENT_ROOT}/client/api/__init__.py"
PYTHONPATH="$(dirname ${SCRIPT_ROOT})" python "${SCRIPT_ROOT}/add__all__.py" "${CLIENT_ROOT}/client/__init__.py"

echo ">>> Done."
