#!/bin/bash

INSTRUCTS_DIR="instructs"
SCRIPT="src/ex7.1.py"
NUM_BITS=4

for file in $INSTRUCTS_DIR/test*.txt; do
    echo "Running $(basename "$file"):"
    python "$SCRIPT" $NUM_BITS "$file"
done
