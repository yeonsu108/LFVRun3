#!/bin/bash
if [ -z "$1" ]
then
    echo "No Input Argument"
else
    target=${1}
    cd $target
    python ../drawhists.py -Y 18
    python ../drawhists.py -Y 18 -L
    cd ../
fi
