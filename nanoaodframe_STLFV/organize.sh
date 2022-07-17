#!/bin/bash
if [ -z "$1" ] || [ -z "$2" ];then
    if [ -z "$1" ]; then
        echo "!!! No Input Argument !!!"
    elif [ -z "$2" ]; then
        echo "!!! Please Specify Systematics !!!
(norm/jecup/jecdown/puup/pudown/btagup_jes/btagdown_jes/...)"
    fi
else
    pname=$1
    sys=$2
    original_pwd=$(pwd)
    cd ${pname}/${sys}
    
    # Remove Log files.
    rm -rf *.out
    for i in 18 16post 16pre 17; do
        echo Setup ${i} samples
        mkdir -p ${i}/tmp
        mv *${i}*${sys}*.root ${i}
        cd ${i}
        if [ ${sys} == 'nom' ]; then
            mv Run* tmp
            rm -rf tmp/Run${i}_${sys}.root
            hadd Run${i}_${sys}.root tmp/Run${i}*_${sys}*.root
        fi
        if [ $i = 17 ] || [ $i == 18 ]; then
            mv TTToSemi* tmp
            rm -rf tmp/TTToSemiLeptonic_${i}_${sys}.root
            hadd TTToSemiLeptonic_${i}_${sys}.root tmp/TTToSemiLeptonic_${i}_${sys}_*.root
        fi
        cd ../
    done
    if [ ${sys} == 'nom' ]; then

        rm -rf Run2_${sys}.root
        hadd Run2_${sys}.root 16pre/Run16pre_${sys}.root 16post/Run16post_${sys}.root 17/Run17_${sys}.root 18/Run18_${sys}.root
        rm -rf *LFV*.root
        hadd ST_LFV_${sys}.root 1*/ST_LFV*.root
        hadd TT_LFV_${sys}.root 1*/TT_LFV*.root
        rm -rf TTTo2L2Nu_${sys}.root TTToSemiLeptonic_${sys}.root
        hadd TTTo2L2Nu_${sys}.root 1*/TTTo2L2Nu*.root
        hadd TTToSemiLeptonic_${sys}.root 1*/TTToSemiLeptonic*.root
    fi
    cd ${original_pwd}
fi
