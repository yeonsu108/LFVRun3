#!/bin/bash
runs=( run16APV run16 run17 run18 )
cats=( cat1 cat2 )
ops=( c_s c_v c_t u_s u_v u_t )
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
            #higgsCombine_initialFit_combined_16_c_s.MultiDimFit.mH125
#            echo combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doInitialFit -n ${cat}_${run}_${op} -t -1
#            combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doInitialFit -n ${cat}_${run}_${op} -t -1
#            echo combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doFits -n ${cat}_${run}_${op} -t -1
#            combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doFits -n ${cat}_${run}_${op} -t -1
#            echo combineTool.py -M Impacts -m 125 -d ${workroot} -n ${cat}_${run}_${op} -o impacts_${cat}_${run}_${op}.json
#            combineTool.py -M Impacts -m 125 -d ${workroot} -n ${cat}_${run}_${op} -o impacts_${cat}_${run}_${op}.json
#            echo plotImpacts.py -i impacts_${cat}_${run}_${op}.json -o impacts_${cat}_${run}_${op} --label-size 0.04 --left-margin 0.2
#            plotImpacts.py -i impacts_${cat}_${run}_${op}.json -o impacts_${cat}_${run}_${op} --label-size 0.04 --left-margin 0.2

            # New
            echo combineTool.py -M Impacts -d ${workroot} -m 125 --doInitialFit --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n ${cat}_${run}_${op}
            combineTool.py -M Impacts -d ${workroot} -m 125 --doInitialFit --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n ${cat}_${run}_${op}
            echo combineTool.py -M Impacts -d ${workroot} -m 125 --doFits --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n ${cat}_${run}_${op}
            combineTool.py -M Impacts -d ${workroot} -m 125 --doFits --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n ${cat}_${run}_${op}
            echo combineTool.py -M Impacts -d ${workroot} -m 125 -n ${cat}_${run}_${op} -o impacts_${cat}_${run}_${op}.json
            combineTool.py -M Impacts -d ${workroot} -m 125 -n ${cat}_${run}_${op} -o impacts_${cat}_${run}_${op}.json
            echo plotImpacts.py -i impacts_${cat}_${run}_${op}.json -o impacts_${cat}_${run}_${op} --label-size 0.04 --left-margin 0.2
            plotImpacts.py -i impacts_${cat}_${run}_${op}.json -o impacts_${cat}_${run}_${op} --label-size 0.04 --left-margin 0.2
            mv higgsCombine_initialFit_${cat}_${run}_${op}*.root ./impacts
            mv higgsCombine_paramFit_${cat}_${run}_${op}*.root ./impacts
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
        # New
        echo combineTool.py -M Impacts -d ${workroot} -m 125 --doInitialFit --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n combined_${run}_${op}
        combineTool.py -M Impacts -d ${workroot} -m 125 --doInitialFit --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n combined_${run}_${op}
        echo combineTool.py -M Impacts -d ${workroot} -m 125 --doFits --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n combined_${run}_${op}
        combineTool.py -M Impacts -d ${workroot} -m 125 --doFits --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n combined_${run}_${op}
        echo combineTool.py -M Impacts -d ${workroot} -m 125 -n combined_${run}_${op} -o impacts_combined_${run}_${op}.json
        combineTool.py -M Impacts -d ${workroot} -m 125 -n combined_${run}_${op} -o impacts_combined_${run}_${op}.json
        echo plotImpacts.py -i impacts_combined_${run}_${op}.json -o impacts_combined_${run}_${op} --label-size 0.04 --left-margin 0.2
        plotImpacts.py -i impacts_combined_${run}_${op}.json -o impacts_combined_${run}_${op} --label-size 0.04 --left-margin 0.2
#        echo combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doInitialFit -n combined_${run}_${op} -t -1
#        combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doInitialFit -n combined_${run}_${op} -t -1
#        echo combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doFits -n combined_${run}_${op} -t -1
#        combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doFits -n combined_${run}_${op} -t -1
#        echo combineTool.py -M Impacts -m 125 -d ${workroot} -n combined_${run}_${op} -o impacts_combined_${run}_${op}.json
#        combineTool.py -M Impacts -m 125 -d ${workroot} -n combined_${run}_${op} -o impacts_combined_${run}_${op}.json
#        echo plotImpacts.py -i impacts_combined_${run}_${op}.json -o impacts_combined_${run}_${op} --label-size 0.04 --left-margin 0.2
#        plotImpacts.py -i impacts_combined_${run}_${op}.json -o impacts_combined_${run}_${op} --label-size 0.04 --left-margin 0.2
        mv higgsCombine_initialFit_combined_${run}_${op}*.root ./impacts
        mv higgsCombine_paramFit_combined_${run}_${op}*.root ./impacts
        mv impacts_combined_${run}_${op}* ./impacts/plots/
    done
done

for op in "${ops[@]}"; do
    workroot=workspace/combined/workspace_${op}.root
    # New
    echo combineTool.py -M Impacts -d ${workroot} -m 125 --doInitialFit --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n combined_run2_${op}
    combineTool.py -M Impacts -d ${workroot} -m 125 --doInitialFit --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n combined_run2_${op}
    echo combineTool.py -M Impacts -d ${workroot} -m 125 --doFits --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n combined_run2_${op}
    combineTool.py -M Impacts -d ${workroot} -m 125 --doFits --robustFit 1 -t -1 --rMin -5 --rMax 10 --expectSignal 1 --cminDefaultMinimizerStrategy 0 -n combined_run2_${op}
    echo combineTool.py -M Impacts -d ${workroot} -m 125 -n combined_run2_${op} -o impacts_combined_run2_${op}.json
    combineTool.py -M Impacts -d ${workroot} -m 125 -n combined_run2_${op} -o impacts_combined_run2_${op}.json
    echo plotImpacts.py -i impacts_combined_run2_${op}.json -o impacts_combined_run2_${op} --label-size 0.04 --left-margin 0.2
    plotImpacts.py -i impacts_combined_run2_${op}.json -o impacts_combined_run2_${op} --label-size 0.04 --left-margin 0.2
#    echo combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doInitialFit -n combined_run2_${op} -t -1
#    combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doInitialFit -n combined_run2_${op} -t -1
#    echo combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doFits -n combined_run2_${op} -t -1
#    combineTool.py -M Impacts -m 125 -d ${workroot} --robustFit 1 --doFits -n combined_run2_${op} -t -1
#    echo combineTool.py -M Impacts -m 125 -d ${workroot} -n combined_run2_${op} -o impacts_combined_run2_${op}.json
#    combineTool.py -M Impacts -m 125 -d ${workroot} -n combined_run2_${op} -o impacts_combined_run2_${op}.json
#    echo plotImpacts.py -i impacts_combined_run2_${op}.json -o impacts_combined_run2_${op} --label-size 0.04 --left-margin 0.2
#    plotImpacts.py -i impacts_combined_run2_${op}.json -o impacts_combined_run2_${op} --label-size 0.04 --left-margin 0.2
    mv higgsCombine_initialFit_combined_run2_${op}*.root ./impacts
    mv higgsCombine_paramFit_combined_run2_${op}*.root ./impacts
    mv impacts_combined_run2_${op}* ./impacts/plots/
done

mv impacts/plots/*json impacts
