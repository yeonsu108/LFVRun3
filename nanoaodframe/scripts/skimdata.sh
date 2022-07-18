#!/bin/bash
#### SETTINGS ####
version=skim_LFVv8
njobs=56

#### PATHs ####
datadir=/data1/common/NanoAOD/v8_UL/data
tgdir=/data1/common/skimmed_NanoAOD/${version}/data
logdir=/data1/common/skimmed_NanoAOD/${version}/log
mkdir -p "${tgdir}"
mkdir -p "${logdir}"
# 16B ver1 has no golden json passing event.
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre   ${datadir}/Run2016B/SingleMuon/NANOAOD/ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1 ${tgdir}/SingleMuon2016B1 &> ${logdir}/SingleMuon2016B1_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre    ${datadir}/Run2016B/SingleMuon/NANOAOD/ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1 ${tgdir}/SingleMuon2016B2 &> ${logdir}/SingleMuon2016B2_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre    ${datadir}/Run2016C ${tgdir}/SingleMuon2016C &> ${logdir}/SingleMuon2016C_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre    ${datadir}/Run2016D ${tgdir}/SingleMuon2016D &> ${logdir}/SingleMuon2016D_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre    ${datadir}/Run2016E ${tgdir}/SingleMuon2016E &> ${logdir}/SingleMuon2016E_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre    ${datadir}/Run2016F/SingleMuon/NANOAOD/HIPM_UL2016_MiniAODv1_NanoAODv2-v1 ${tgdir}/SingleMuon2016Fpre &> ${logdir}/SingleMuon2016Fpre_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post   ${datadir}/Run2016F/SingleMuon/NANOAOD/UL2016_MiniAODv1_NanoAODv2-v4 ${tgdir}/SingleMuon2016Fpost &> ${logdir}/SingleMuon2016Fpost_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post   ${datadir}/Run2016G ${tgdir}/SingleMuon2016G &> ${logdir}/SingleMuon2016G_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post   ${datadir}/Run2016H ${tgdir}/SingleMuon2016H &> ${logdir}/SingleMuon2016H_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim17       ${datadir}/Run2017B ${tgdir}/SingleMuon2017B &> ${logdir}/SingleMuon2017B_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim17       ${datadir}/Run2017C ${tgdir}/SingleMuon2017C &> ${logdir}/SingleMuon2017C_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim17       ${datadir}/Run2017D ${tgdir}/SingleMuon2017D &> ${logdir}/SingleMuon2017D_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim17       ${datadir}/Run2017E ${tgdir}/SingleMuon2017E &> ${logdir}/SingleMuon2017E_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim17       ${datadir}/Run2017F ${tgdir}/SingleMuon2017F &> ${logdir}/SingleMuon2017F_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim18       ${datadir}/Run2018A/SingleMuon ${tgdir}/SingleMuon2018A &> ${logdir}/SingleMuon2018A_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim18       ${datadir}/Run2018B/SingleMuon ${tgdir}/SingleMuon2018B &> ${logdir}/SingleMuon2018B_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim18       ${datadir}/Run2018C/SingleMuon ${tgdir}/SingleMuon2018C &> ${logdir}/SingleMuon2018C_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim18       ${datadir}/Run2018D/SingleMuon ${tgdir}/SingleMuon2018D &> ${logdir}/SingleMuon2018D_skim.out
