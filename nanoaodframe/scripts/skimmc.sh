#!/bin/bash
#### SETTINGS ####
version=skim_LFVv8
#year=$1
njobs=$1


for year in "16pre" "16post" "17" "18"
do
    #### PATHs ####
    camp=""
    if [ $year == "16pre" ]; then
        camp="RunIISummer20UL16NanoAODAPVv2"
    elif [ $year == "16post" ]; then
        camp="RunIISummer20UL16NanoAODv2"
    else
        camp="RunIISummer20UL${year}NanoAODv2"
    fi

    mcdir=/data1/common/NanoAOD/v8_UL/mc/${camp}
    tgdir=/data1/common/skimmed_NanoAOD/${version}/mc/${year}
    log=/data1/common/skimmed_NanoAOD/${version}/log

    mkdir -p "${tgdir}"
    mkdir -p "${log}"

    # QCD NanoAOD Dataset names are not consistent.
    if [ $year == "16pre" ]; then
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV_pythia8 ${tgdir}/QCD_Pt-15To20_MuEnrichedPt5 &> ${log}/QCD_Pt-15To20_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV_pythia8 ${tgdir}/QCD_Pt-80To120_MuEnrichedPt5 &> ${log}/QCD_Pt-80To120_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV_pythia8 ${tgdir}/QCD_Pt-120To170_MuEnrichedPt5 &> ${log}/QCD_Pt-120To170_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV_pythia8 ${tgdir}/QCD_Pt-170To300_MuEnrichedPt5 &> ${log}/QCD_Pt-170To300_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV_pythia8 ${tgdir}/QCD_Pt-470To600_MuEnrichedPt5 &> ${log}/QCD_Pt-470To600_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8 ${tgdir}/QCD_Pt-800To1000_MuEnrichedPt5 &> ${log}/QCD_Pt-800To1000_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8 ${tgdir}/QCD_Pt-1000_MuEnrichedPt5 &> ${log}/QCD_Pt-1000_MuEnrichedPt5_skim${year}.out
    else
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-15To20_MuEnrichedPt5 &> ${log}/QCD_Pt-15To20_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-80To120_MuEnrichedPt5 &> ${log}/QCD_Pt-80To120_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-120To170_MuEnrichedPt5 &> ${log}/QCD_Pt-120To170_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-170To300_MuEnrichedPt5 &> ${log}/QCD_Pt-170To300_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-470To600_MuEnrichedPt5 &> ${log}/QCD_Pt-470To600_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-800To1000_MuEnrichedPt5 &> ${log}/QCD_Pt-800To1000_MuEnrichedPt5_skim${year}.out
        ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-1000_MuEnrichedPt5 &> ${log}/QCD_Pt-1000_MuEnrichedPt5_skim${year}.out
    fi
    ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-20To30_MuEnrichedPt5 &> ${log}/QCD_Pt-20To30_MuEnrichedPt5_skim${year}.out
    ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-30To50_MuEnrichedPt5 &> ${log}/QCD_Pt-30To50_MuEnrichedPt5_skim${year}.out
    ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-50To80_MuEnrichedPt5 &> ${log}/QCD_Pt-50To80_MuEnrichedPt5_skim${year}.out
    ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-300To470_MuEnrichedPt5 &> ${log}/QCD_Pt-300To470_MuEnrichedPt5_skim${year}.out
    ./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir}/QCD_Pt-600To800_MuEnrichedPt5 &> ${log}/QCD_Pt-600To800_MuEnrichedPt5_skim${year}.out
done

./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir}/DYJetsToLL_M-10to50 &> ${log}/DYJetsToLL_M-10to50_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8 ${tgdir}/DYJetsToLL_M-50_amcatnlo  &> ${log}/DYJetsToLL_M-50_amcatnlo_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir}/DYJetsToLL_M-50_madgraph &> ${log}/DYJetsToLL_M-50_madgraph_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8 ${tgdir}/ST_t-channel_antitop &> ${log}/ST_t-channel_antitop_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8 ${tgdir}/ST_t-channel_top &> ${log}/ST_t-channel_top_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8 ${tgdir}/ST_tW_antitop &> ${log}/ST_tW_antitop_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8 ${tgdir}/ST_tW_top &> ${log}/ST_tW_top_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8 ${tgdir}/TTTo2L2Nu &> ${log}/TTTo2L2Nu_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/TTToHadronic_TuneCP5_13TeV-powheg-pythia8 ${tgdir}/TTToHadronic &> ${log}/TTToHadronic_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8 ${tgdir}/TTToSemiLeptonic &> ${log}/TTToSemiLeptonic_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8 ${tgdir}/TTWJetsToLNu &> ${log}/TTWJetsToLNu_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8 ${tgdir}/TTWJetsToQQ &> ${log}/TTWJetsToQQ_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8 ${tgdir}/TTZToLLNuNu &> ${log}/TTZToLLNuNu_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8 ${tgdir}/TTZToQQ &> ${log}/TTZToQQ_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y wjetskim${year} ${mcdir}/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir}/WJetsToLNu_HT-0To100 &> ${log}/WJetsToLNu_HT-0To100_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir}/WJetsToLNu_HT-100To200 &> ${log}/WJetsToLNu_HT-100To200_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir}/WJetsToLNu_HT-200To400 &> ${log}/WJetsToLNu_HT-200To400_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir}/WJetsToLNu_HT-400To600 &> ${log}/WJetsToLNu_HT-400To600_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir}/WJetsToLNu_HT-600To800 &> ${log}/WJetsToLNu_HT-600To800_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir}/WJetsToLNu_HT-800To1200 &> ${log}/WJetsToLNu_HT-800To1200_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir}/WJetsToLNu_HT-1200To2500 &> ${log}/WJetsToLNu_HT-1200To2500_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir}/WJetsToLNu_HT-2500ToInf &> ${log}/WJetsToLNu_HT-2500ToInf_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/WW_TuneCP5_13TeV-pythia8 ${tgdir}/WW &> ${log}/WW_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/WZ_TuneCP5_13TeV-pythia8 ${tgdir}/WZ &> ${log}/WZ_skim${year}.out
./skimnanoaod.py -F --split ${njobs} -Y skim${year} ${mcdir}/ZZ_TuneCP5_13TeV-pythia8 ${tgdir}/ZZ &> ${log}/ZZ_skim${year}.out
