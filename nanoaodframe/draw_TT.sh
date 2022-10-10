#!/bin/bash
if [ -z "$1" ]
then
    echo "No Input Argument"
else
    target=${1}
    sys=$2
    mkdir -p plot_TTLFV/$target/noblind
    mkdir -p plot_TTLFV/$target/blind
    rm -rf plot_TTLFV/$target/*/plot*
    rm -rf plot_TTLFV/$target/*/*.root
    cd $target
    for i in run2 16pre 16post 17 18
    #for i in run2
    do
        python ../drawhists.py -Y $i -SYS $sys
        python ../drawhists.py -Y $i -L -SYS $sys
        mv plot* ../plot_TTLFV/$target/noblind
        mv stackhist* ../plot_TTLFV/$target/noblind

        python ../drawhists.py -B -Y $i -SYS $sys
        python ../drawhists.py -B -Y $i -L -SYS $sys
        mv plot* ../plot_TTLFV/$target/blind
        mv stackhist* ../plot_TTLFV/$target/blind
    done
    cd ../
fi
