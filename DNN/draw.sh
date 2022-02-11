#!/bin/bash
if [ -z "$1" ]
then
    echo "No Input Argument"
else
    systs=( norm jecup jecdown puup pudown btagup_jes btagdown_jes btagup_hf btagdown_hf btagup_lf btagdown_lf )
    for syst in "${systs[@]}"; do
        cd ${1}/${syst}/pred_hists/
        rm -rf Run2_${syst}_pred.root
        hadd Run2_${syst}_pred.root 1*/Run*.root
        rm -rf plot* stack*.root
        for i in run2 16pre 16post 17 18
        do
            python ../../../drawhists.py -SYS ${syst} -Y $i
            python ../../../drawhists.py -SYS ${syst} -Y $i -L
        done
        cd -
    done
fi
