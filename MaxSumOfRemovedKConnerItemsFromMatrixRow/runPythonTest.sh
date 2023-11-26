#!/bin/bash
ALGO_HOME=$(dirname "$(realpath $0)")
TEST_PATH="${ALGO_HOME}/test.py"
python3 "${TEST_PATH}"
