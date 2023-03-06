#!/bin/bash
runs=( run16APV run16 run17 run18 )
cats=( cat1 cat2 )
ops=( c_s c_v c_t u_s u_v u_t )
labelsize=0.05
margin_l=0.4
if [ ! -d ./impacts/plots ]; then
    mkdir -p ./impacts/plots
fi
for run in "${runs[@]}"; do
    for cat in "${cats[@]}"; do
        if [ ! -d results/${cat}/${run} ]; then
            mkdir -p results/${cat}/${run}
        fi
        for op in "${ops[@]}"; do
            workroot=workspace/${cat}/${run}/workspace_${op}.root
            plotImpacts.py -i ./impacts/impacts_${cat}_${run}_${op}.json -o impacts_${cat}_${run}_${op} --label-size ${labelsize} --left-margin ${margin_l}
            mv impacts_${cat}_${run}_${op}* ./impacts/plots/
        done
    done
done

for run in "${runs[@]}"; do
    if [ ! -d results/combined/${run} ]; then
        mkdir -p results/combined/${run}
    fi
    for op in "${ops[@]}"; do
        workroot=workspace/combined/${run}/workspace_${op}.root
        plotImpacts.py -i ./impacts/impacts_combined_${run}_${op}.json -o impacts_combined_${run}_${op} --label-size ${labelsize} --left-margin ${margin_l}
        mv impacts_combined_${run}_${op}* ./impacts/plots/
    done
done

for op in "${ops[@]}"; do
    workroot=workspace/combined/workspace_${op}.root
    plotImpacts.py -i ./impacts/impacts_combined_run2_${op}.json -o impacts_combined_run2_${op} --label-size ${labelsize} --left-margin ${margin_l}
    mv impacts_combined_run2_${op}* ./impacts/plots/
done
