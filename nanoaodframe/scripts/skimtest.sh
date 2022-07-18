#!/bin/bash
#### SETTINGS ####
njobs=56

#### PATHs ####
datadir=/data1/common/NanoAOD/v8_UL/data
mcdir20ul18=/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL18NanoAODv2
tgdir=$(pwd)
logdir=$(pwd)
mkdir -p ${tgdir18}
mkdir -p ${logdir}

# Test for skimnanoaod.py
# DATA
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${datadir}/Run2016F/SingleMuon/NANOAOD/UL2016_MiniAODv1_NanoAODv2-v4 ${tgdir}/SingleMuon2016Fpost &> ${logdir}/SingleMuon2016Fpost_skim.out &

# MC
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8 ${tgdir}/ST_t-channel_top &> ${logdir}/ST_t-channel_top_skim18.out &
