#!/bin/bash
ALGO_HOME=$(dirname "$(realpath $0)")
TEST_PATH="${ALGO_HOME}/test.js"
node "${TEST_PATH}"
