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

set -o errexit
set -o nounset
set -o pipefail

ENV=${VIRTUAL_ENV:-}

if [[ -z ${ENV} ]]; then
    if ! which virtualenv > /dev/null 2>&1; then
      echo "virtualenv is not installed. run: [sudo] pip install virtualenv"
      exit
    fi
fi

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
REPO_ROOT="${SCRIPT_ROOT}/../"
CLIENT_ROOT="${REPO_ROOT}/kubernetes_asyncio"

pushd "${SCRIPT_ROOT}" > /dev/null
if [[ -z ${ENV} ]]; then
    echo "--- Creating virtualenv"
    virtualenv "${SCRIPT_ROOT}/.py"

    VIRTUAL_ENV_DISABLE_PROMPT=1; source "${SCRIPT_ROOT}/.py/bin/activate"
    trap "deactivate" EXIT SIGINT

    echo "--- Updating tools"
    pip install --upgrade flake8 isort
fi

# Style checks.
flake8
isort -c
popd

echo "---Done."
