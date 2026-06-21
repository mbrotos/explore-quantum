#!/bin/bash

INSTRUCTS_DIR="resources/instructs"
SCRIPT="src/ex7_1.py"
NUM_BITS=4

for file in "$INSTRUCTS_DIR"/test[0-9]*.txt; do
    echo "Running $(basename "$file"):"
    python "$SCRIPT" --num-bits "$NUM_BITS" --instructions "$file"
done
