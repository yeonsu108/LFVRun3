#!/bin/bash
#combine --run blind -M AsymptoticLimits workspace/workspace_c_s.root -m 800 -n c_s
#combine --run blind -M AsymptoticLimits workspace/ST/workspace_u_t.root -m 800 -n STu_t --rMax 0.01 -v 2 
runs=( run16APV run16 run17 run18 )
cats=( cat1 cat2 )
ops=( c_s c_v c_t u_s u_v u_t )
for run in "${runs[@]}"; do
    for cat in "${cats[@]}"; do
        if [ ! -d results/${cat}/${run} ]; then
            mkdir -p results/${cat}/${run}
        fi
        for op in "${ops[@]}"; do
            workroot=workspace/${cat}/${run}/workspace_${op}.root
            echo combine --run blind -M AsymptoticLimits ${workroot} -m 800 -n ${run}${cat}${op}
            combine --run blind -M AsymptoticLimits ${workroot} -m 800 -n ${run}${cat}${op}
            mv higgsCombine${run}${cat}${op}.AsymptoticLimits.mH800.root results/${cat}/${run}
        done
    done
done

for run in "${runs[@]}"; do
    if [ ! -d results/combined/${run} ]; then
        mkdir -p results/combined/${run}
    fi
    for op in "${ops[@]}"; do
        workroot=workspace/combined/${run}/workspace_${op}.root
        echo combine --run blind -M AsymptoticLimits ${workroot} -m 800 -n Combined${run}${op}
        combine --run blind -M AsymptoticLimits ${workroot} -m 800 -n Combined${run}${op}
        mv higgsCombineCombined${run}${op}.AsymptoticLimits.mH800.root results/${run}
    done
done

for cat in "${cats[@]}"; do
    for op in "${ops[@]}"; do
        if [ ! -d results/combined/${cat} ]; then
            mkdir -p results/combined/${cat}
        fi
        workroot=workspace/combined/${cat}/workspace_${op}.root
        echo combine --run blind -M AsymptoticLimits ${workroot} -m 800 -n Combinedrun2${cat}${op}
        combine --run blind -M AsymptoticLimits ${workroot} -m 800 -n Combinedrun2${cat}${op}
        mv higgsCombineCombinedrun2${cat}${op}.AsymptoticLimits.mH800.root results/
    done
done

for op in "${ops[@]}"; do
    workroot=workspace/combined/workspace_${op}.root
    echo combine --run blind -M AsymptoticLimits ${workroot} -m 800 -n Combinedrun2${op}
    combine --run blind -M AsymptoticLimits ${workroot} -m 800 -n Combinedrun2${op}
    mv higgsCombineCombinedrun2${op}.AsymptoticLimits.mH800.root results/
done
