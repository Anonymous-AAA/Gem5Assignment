#!/bin/bash

set -e

assocs=("2" "4" "8" "512")
policy=("RandomRP" "LRURP" "FIFORP" "MRURP")

M5_FOLDER="/home/anonymousa/gem5_sim/gem5/m5out"
DESTINATION_BASE="/home/anonymousa/gem5_sim/gem5/my_impl/proj/stats"

# Loop through all possible combinations of arguments
for arg1 in {0..3}; do
    for arg2 in {0..3}; do
        echo "Executing with arguments: $arg1 $arg2"
        #./p "$arg1" "$arg2"
        build/X86/gem5.opt my_impl/proj/arg_ass.py --assoc "$arg1" --repl "$arg2"
        cp -r "$M5_FOLDER" "$DESTINATION_BASE/${assocs[$arg1]}_${policy[$arg2]}"
        echo "---------------------------------"
    done
done
