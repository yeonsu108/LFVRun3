#!/bin/bash
#combine --run blind -M AsymptoticLimits workspace/workspace_c_s.root -m 800 -n c_s
#combine --run blind -M AsymptoticLimits workspace/ST/workspace_u_t.root -m 800 -n STu_t --rMax 0.01 -v 2 
runs=( run16APV run16 run17 run18 )
cats=( cat1 cat2 )
ops=( c_s c_v c_t u_s u_v u_t )
mkdir logs
for run in "${runs[@]}"; do
    for cat in "${cats[@]}"; do
        if [ ! -d results/${cat}/${run} ]; then
            mkdir -p results/${cat}/${run}
        fi
        for op in "${ops[@]}"; do
            workroot=workspace/${cat}/${run}/workspace_${op}.root
            if [ ${cat}${op} == cat1u_t ]; then
                echo combine --run blind -M AsymptoticLimits ${workroot} -n ${run}${cat}${op} --rMin 0.001 --rMax 0.1 > logs/result_${cat}_${run}_${op}.txt
                combine --run blind -M AsymptoticLimits ${workroot} -n ${run}${cat}${op} --rMin 0.001 --rMax 0.1 >> logs/result_${cat}_${run}_${op}.txt
            else
                echo combine --run blind -M AsymptoticLimits ${workroot} -n ${run}${cat}${op} > logs/result_${cat}_${run}_${op}.txt
                combine --run blind -M AsymptoticLimits ${workroot} -n ${run}${cat}${op} >> logs/result_${cat}_${run}_${op}.txt
            fi
            mv higgsCombine${run}${cat}${op}.AsymptoticLimits.mH120.root results/${cat}/${run}
        done
    done
done

for run in "${runs[@]}"; do
    if [ ! -d results/combined/${run} ]; then
        mkdir -p results/combined/${run}
    fi
    for op in "${ops[@]}"; do
        workroot=workspace/combined/${run}/workspace_${op}.root
        if [ ${run}${op} == run18u_t ]; then
            echo combine --run blind -M AsymptoticLimits ${workroot} -n Combined${run}${op} --rMax 0.1 --rMin 0.00001 > logs/result_combined_${run}_${op}.txt
            combine --run blind -M AsymptoticLimits ${workroot} -n Combined${run}${op} --rMax 0.1 --rMin 0.00001 >> logs/result_combined_${run}_${op}.txt
        elif [ ${op} == u_t ]; then
            echo combine --run blind -M AsymptoticLimits ${workroot} -n Combined${run}${op} --rMax 0.01 --rMin 0.001 > logs/result_combined_${run}_${op}.txt
            combine --run blind -M AsymptoticLimits ${workroot} -n Combined${run}${op} --rMax 0.01 --rMin 0.001 >> logs/result_combined_${run}_${op}.txt
        else
            echo combine --run blind -M AsymptoticLimits ${workroot} -n Combined${run}${op} > logs/result_combined_${run}_${op}.txt
            combine --run blind -M AsymptoticLimits ${workroot} -n Combined${run}${op} >> logs/result_combined_${run}_${op}.txt
        fi
        mv higgsCombineCombined${run}${op}.AsymptoticLimits.mH120.root results/combined/${run}
    done
done

for op in "${ops[@]}"; do
    workroot=workspace/combined/workspace_${op}.root
    if [ ${op} == u_t ]; then
        echo combine --run blind -M AsymptoticLimits ${workroot} -n Combinedrun2${op} --rMin 0.0002 > logs/result_combined_run2_${op}.txt
        combine --run blind -M AsymptoticLimits ${workroot} -n Combinedrun2${op} --rMin 0.0002 >> logs/result_combined_run2_${op}.txt
    else
        echo combine --run blind -M AsymptoticLimits ${workroot} -n Combinedrun2${op} > logs/result_combined_run2_${op}.txt
        combine --run blind -M AsymptoticLimits ${workroot} -n Combinedrun2${op} >> logs/result_combined_run2_${op}.txt
    fi
    mv higgsCombineCombinedrun2${op}.AsymptoticLimits.mH120.root results/combined/
done
