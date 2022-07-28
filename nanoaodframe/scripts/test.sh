#!/bin/bash
#### SETTINGS ####
njobs=56

#### PATHs ####
datadir=/data1/common/NanoAOD/v8_UL/data
mcdir=/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL18NanoAODv2
json16=data/GoldenJSON/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt
json17=data/GoldenJSON/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt
json18=data/GoldenJSON/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt

# Syst : nom, jecup, jecdown, puup, pudown, btagup_jes, btagdown_jes
syst=nom

tgdir=$(pwd)
logdir=$(pwd)
mkdir -p ${tgdir}
mkdir -p ${logdir}

# 1. Test for skimnanoaod.py
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${datadir}/Run2016F/SingleMuon/NANOAOD/UL2016_MiniAODv1_NanoAODv2-v4 ${tgdir}/SingleMuon2016Fpost &> ${logdir}/SingleMuon2016Fpost_skim.out &
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir}/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8 ${tgdir}/ST_t-channel_top &> ${logdir}/ST_t-channel_top_skim18.out &

# 2. Test for processnanoaod.py with skimmed samples.
./processnanoaod_ST.py -A -Y 16post -S ${syst} --globaltag Summer19UL16_RunFGH_V7 -J ${json16} ./SingleMuon2016Fpost test_process_Run16postF_${syst}.root   &> test_process_Run16postF_${syst}.out &
./processnanoaod_ST.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ./ST_t-channel_top test_process_ST_t-channel_top_18_${syst}.root &> test_process_ST_t-channel_top_18_${syst}.out &

# Test for processonefile.py with an existing skimmed file.
./processonefile.py -Y 18 -S ${syst} --globaltag Summer19UL16APV_V7 /data1/common/skimmed_NanoAOD/skim_LFVv8/mc/18/TTTo2L2Nu/270000_019426EE-3D50-1249-B266-F6DBA0AFE3B5_analyzed.root test_process_mc_TTTo2L2Nu.root outputTree outputTree2 &> test_process_mc_TTTo2L2Nu.out

