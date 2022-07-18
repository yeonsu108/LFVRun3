#!/bin/bash
#### SETTINGS ####
version=skim_testLFV_v9
njobs=10

#### PATHs ####
datadir=/data1/common/NanoAOD/v8_UL/data
tgdir=/data1/common/skimmed_NanoAOD/${version}/data
logdir=/data1/common/skimmed_NanoAOD/${version}/log
tgdir=$(pwd)
logdir=$(pwd)
mkdir -p "${tgdir}"
mkdir -p "${logdir}"
./skimnanoaod.py -F --split ${njobs} -Y skim16post   ${datadir}/Run2016F/SingleMuon/NANOAOD/UL2016_MiniAODv1_NanoAODv2-v4 ${tgdir}/SingleMuon2016Fpost &> ${logdir}/SingleMuon2016Fpost_skim.out &
