#!/bin/bash
ALGO_HOME=$(dirname "$(realpath $0)")
ALGO_NAME=$(basename "${ALGO_HOME}")
PROJECT_HOME=$(dirname "${ALGO_HOME}")
PROJECT_NAME=$(basename "${PROJECT_HOME}")
PROJECT_BUILD="${PROJECT_HOME}_build"
TEST_PATH="${PROJECT_BUILD}/${PROJECT_NAME}/bin/${ALGO_NAME}"
cd "${PROJECT_HOME}"
make
cd -
"${TEST_PATH}"
