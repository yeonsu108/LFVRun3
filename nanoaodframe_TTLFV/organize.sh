#!/bin/bash
pname=$1
if [ -z "$1" ]
then
    echo "No Input Argument"
else
    sys=$2
    cd ${pname}
    rm -rf *.out
    for i in 18 16post 16pre 17
    do
        echo Setup ${i} samples
        mkdir -p ${i}/tmp
        mv *${i}*${sys}*.root ${i}
        cd ${i}
        mv Run* tmp
        rm -rf tmp/Run${i}_${sys}.root
        hadd Run${i}_${sys}.root tmp/Run${i}*_${sys}*.root
        if [ $i = 17 ] || [ $i == 18 ]
        then
            mv TTToSemi* tmp
            rm -rf tmp/TTToSemiLeptonic_${i}_${sys}.root
            hadd TTToSemiLeptonic_${i}_${sys}.root tmp/TTToSemiLeptonic_${i}_${sys}_*.root
        fi
        mv tmp/Run20${i}_${sys}.root tmp/TTToSemiLeptonic_${i}_${sys}.root ./
        cd ../
    done
    rm -rf Run2_${sys}.root
    hadd Run2_${sys}.root 16pre/Run16pre_${sys}.root 16post/Run16post_${sys}.root 17/Run17_${sys}.root 18/Run18_${sys}.root
    rm -rf *LFV*.root
    hadd ST_LFV_${sys}.root 18/ST_LFV*.root
    hadd TT_LFV_${sys}.root 18/TT_LFV*.root
    rm -rf TTTo2L2Nu_${sys}.root TTToSemiLeptonic_${sys}.root
    hadd TTTo2L2Nu_${sys}.root 1*/TTTo2L2Nu*.root
    hadd TTToSemiLeptonic_${sys}.root 1*/TTToSemiLeptonic*.root
    cd ../
fi
