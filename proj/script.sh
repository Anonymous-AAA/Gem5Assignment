#!/bin/bash

set -e

# Loop through all possible combinations of arguments
for arg1 in {0..3}; do
    for arg2 in {0..3}; do
        echo "Executing with arguments: $arg1 $arg2"
        #./p "$arg1" "$arg2"
        build/X86/gem5.opt my_impl/proj/arg_ass.py --assoc "$arg1" --repl "$arg2"
        echo "---------------------------------"
    done
done
