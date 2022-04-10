#!/bin/bash
#text2workspace.py datacards/datacard_c_s.txt -m 800 -o workspace/workspace_c_s.root
runs=( run16APV run16 run17 run18 )
cats=( cat1 cat2 )
ops=( c_s c_v c_t u_s u_v u_t )
for run in "${runs[@]}"; do
    for cat in "${cats[@]}"; do
        if [ ! -d workspace/${cat}/${run} ]; then
            mkdir -p workspace/${cat}/${run}
        fi
        for op in "${ops[@]}"; do
            datacard=datacards/datacard_${cat}_${run}_${op}.txt
            output=workspace/${cat}/${run}/workspace_${op}.root
            echo text2workspace.py ${datacard} -m 800 -o ${output}
            text2workspace.py ${datacard} -m 800 -o ${output}
        done
    done
done
for run in "${runs[@]}"; do
    if [ ! -d workspace/combined/${run} ]; then
        mkdir -p workspace/combined/${run}
    fi
    for op in "${ops[@]}"; do
        datacard=datacards/combined_${run}_datacard_${op}.txt
        output=workspace/combined/${run}/workspace_${op}.root
        echo text2workspace.py ${datacard} -m 800 -o ${output}
        text2workspace.py ${datacard} -m 800 -o ${output}
    done
done

for op in "${ops[@]}"; do
    datacard=datacards/combined_run2_datacard_${op}.txt
    output=workspace/combined/workspace_${op}.root
    echo text2workspace.py ${datacard} -m 800 -o ${output}
    text2workspace.py ${datacard} -m 800 -o ${output}
done
