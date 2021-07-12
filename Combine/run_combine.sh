#!/bin/bash
datacard_path=st_datacards/datacard_countingLFV
processes=(stc stu ttc ttu)
operators=(s v t)
ext=18.txt
for p in ${processes[*]}; do
    for op in ${operators[*]}; do
        card=${datacard_path}${p}_${op}_${ext}
        echo ${p}_${op} >> combinelog.txt
        combine ${card} --run blind -n .${p}_${op} >> combinelog.txt
        echo "" >> combinelog.txt
        echo "######################################" >> combinelog.txt
        echo "" >> combinelog.txt
    done
done
