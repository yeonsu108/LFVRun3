#!/bin/bash
datacard_path=datacards/datacard_countingLFV
runs=(16 17 18)
processes=(stc stu ttc ttu)
operators=(s v t)
rmaxs=(3.0 3.0 3.0 3.0 1.0 0.1 100 100 100 100 100 100)
# stc  s   v   t stus  v   t ttcs  v   t ttus  v   t
ext=.txt
for run in ${runs[*]}; do
    i=0
    for p in ${processes[*]}; do
        for op in ${operators[*]}; do
            card=${datacard_path}${p}_${op}_${run}${ext}
            echo "Command : combine ${card} --run blind -n .${p}_${op}_${run} --rMin 0.0001 --rMax ${rmaxs[i]}" >> combinelog.txt
            combine ${card} --run blind -n .${p}_${op}_${run} --rMin 0.0001 --rMax ${rmaxs[i]}>> combinelog.txt
            echo "" >> combinelog.txt
            echo "######################################" >> combinelog.txt
            echo "" >> combinelog.txt
            i=$((i+1))
        done
    done
done
