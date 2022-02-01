#!/bin/bash
runs=( "run16APV" "run16" "run17" "run18" )
label="jan01"
cats=( "cat1" "cat2" )
ops=( "c_s" "c_v" "c_t" "u_s" "u_v" "u_t" )
for cat in "${cats[@]}"; do
    for run in "${runs[@]}"; do
        for op in "${ops[@]}"; do
            rfile="pred_"${run}"_"${cat}".root"
            target=datacard_${cat}_${run}_${op}.txt
            sed 's/rootfilehere/'${label}'\/'${rfile}'/' src/datacard_${run}.txt > ${target}
            sed -i 's/opt/'${op}'/g' ${target}
            # No DY events for cat1 run16
            if [ ${cat}${run} == cat1run16 ]; then
                sed -i 's/rate                    -1         -1         -1     -1     -1/rate                    -1         -1         -1     -1     0/' ${target}
            fi
        done
    done
done

for run in "${runs[@]}"; do
    for op in "${ops[@]}"; do
        combineCards.py cat1=datacard_cat1_${run}_${op}.txt cat2=datacard_cat2_${run}_${op}.txt > combined_${run}_datacard_${op}.txt
    done
done

for cat in "${cats[@]}"; do
    for op in "${ops[@]}"; do
        combineCards.py run16APV=datacard_${cat}_run16APV_${op}.txt run16=datacard_${cat}_run16_${op}.txt run17=datacard_${cat}_run17_${op}.txt run18=datacard_${cat}_run18_${op}.txt > combined_run2_datacard_${cat}_${op}.txt
    done
done

for op in "${ops[@]}"; do
    combineCards.py run16APV=combined_run16APV_datacard_${op}.txt run16=combined_run16_datacard_${op}.txt run17=combined_run17_datacard_${op}.txt run18=combined_run18_datacard_${op}.txt > combined_run2_datacard_${op}.txt
done
