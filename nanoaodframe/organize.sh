#!/bin/bash
#if [ -z "$1" ] || [ -z "$2" ];then
if [ -z "$1" ]; then
    echo "!!! No Input Argument !!!"
elif [ ! -d "$1" ]; then
    echo "!!! Invalid input path !!!"
#    elif [ -z "$2" ]; then
#        echo "!!! Please Specify Systematics !!!
#(norm/jecup/jecdown/puup/pudown/btagup_jes/btagdown_jes/...)"
else
    pname=$1
    systs=( nom puup pudown btagup_hf btagdown_hf btagup_lf btagdown_lf \
        btagup_hfstats1 btagdown_hfstats1 btagup_hfstats2 btagdown_hfstats2 \
        btagup_lfstats1 btagdown_lfstats1 btagup_lfstats2 btagdown_lfstats2 \
        btagup_cferr1 btagdown_cferr1 btagup_cferr2 btagdown_cferr2 \
        up_jesAbsolute down_jesAbsolute up_jesAbsolute_year down_jesAbsolute_year \
        up_jesBBEC1 down_jesBBEC1 up_jesBBEC1_year down_jesBBEC1_year \
        up_jesEC2 down_jesEC2 up_jesEC2_year down_jesEC2_year \
        up_jesFlavorQCD down_jesFlavorQCD up_jesRelativeBal down_jesRelativeBal \
        up_jesRelativeSample_year down_jesRelativeSample_year )
    echo "List of systematics"
    for syst in "${systs[@]}"; do
        echo $syst
        original_pwd=$(pwd)
        cd ${pname}/${syst}
        
        # Remove Log files.
        rm -rf *.out
        for i in 18 16post 16pre 17; do
            echo Setup ${i} samples
            mkdir -p ${i}/tmp
            mv *${i}*${syst}*.root ${i}
            cd ${i}
            if [ ${syst} == 'nom' ]; then
                mv Run* tmp
                rm -rf tmp/Run${i}_${syst}.root
                hadd Run${i}_${syst}.root tmp/Run${i}*_${syst}*.root
            fi
            if [ $i = 17 ] || [ $i == 18 ]; then
                mv TTToSemi* tmp
                rm -rf tmp/TTToSemiLeptonic_${i}_${syst}.root
                hadd TTToSemiLeptonic_${i}_${syst}.root tmp/TTToSemiLeptonic_${i}_${syst}_*.root
            fi
            cd ../
        done
        if [ ${syst} == 'nom' ]; then

            rm -rf Run2_${syst}.root
            hadd Run2_${syst}.root 16pre/Run16pre_${syst}.root 16post/Run16post_${syst}.root 17/Run17_${syst}.root 18/Run18_${syst}.root
            rm -rf *LFV*.root
            hadd ST_LFV_${syst}.root 1*/ST_LFV*.root
            hadd TT_LFV_${syst}.root 1*/TT_LFV*.root
            rm -rf TTTo2L2Nu_${syst}.root TTToSemiLeptonic_${syst}.root
            hadd TTTo2L2Nu_${syst}.root 1*/TTTo2L2Nu*.root
            hadd TTToSemiLeptonic_${syst}.root 1*/TTToSemiLeptonic*.root
        fi
    cd ${original_pwd}
    done
fi
