#!/bin/bash
#### SETTINGS ####
version=skim_LFVv8
njobs=28

#### PATHs ####
datadir=/data1/common/NanoAOD/v8_UL/data
tgdir=/data1/common/skimmed_NanoAOD/${version}/data
log=/data1/common/skimmed_NanoAOD/${version}/log
mkdir -p "${tgdir}"
mkdir -p "${log}"
# 16B ver1 has no golden json passing event.
#./skimnanoaod.py -F --split ${njobs} -Y skim16pre  ${datadir}/Run2016B/SingleMuon/NANOAOD/ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1 ${tgdir}/SingleMuon2016B1 &> ${log}/SingleMuon2016B1_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre  ${datadir}/Run2016B/SingleMuon/NANOAOD/ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1 ${tgdir}/SingleMuon2016B2 &> ${log}/SingleMuon2016B2_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre  ${datadir}/Run2016C/SingleMuon ${tgdir}/SingleMuon2016C &> ${log}/SingleMuon2016C_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre  ${datadir}/Run2016D/SingleMuon ${tgdir}/SingleMuon2016D &> ${log}/SingleMuon2016D_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre  ${datadir}/Run2016E/SingleMuon ${tgdir}/SingleMuon2016E &> ${log}/SingleMuon2016E_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16pre  ${datadir}/Run2016F/SingleMuon/NANOAOD/HIPM_UL2016_MiniAODv1_NanoAODv2-v1 ${tgdir}/SingleMuon2016Fpre &> ${log}/SingleMuon2016Fpre_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${datadir}/Run2016F/SingleMuon/NANOAOD/UL2016_MiniAODv1_NanoAODv2-v4 ${tgdir}/SingleMuon2016Fpost &> ${log}/SingleMuon2016Fpost_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${datadir}/Run2016G/SingleMuon ${tgdir}/SingleMuon2016G &> ${log}/SingleMuon2016G_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim16post ${datadir}/Run2016H/SingleMuon ${tgdir}/SingleMuon2016H &> ${log}/SingleMuon2016H_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim17     ${datadir}/Run2017B/SingleMuon ${tgdir}/SingleMuon2017B &> ${log}/SingleMuon2017B_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim17     ${datadir}/Run2017C/SingleMuon ${tgdir}/SingleMuon2017C &> ${log}/SingleMuon2017C_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim17     ${datadir}/Run2017D/SingleMuon ${tgdir}/SingleMuon2017D &> ${log}/SingleMuon2017D_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim17     ${datadir}/Run2017E/SingleMuon ${tgdir}/SingleMuon2017E &> ${log}/SingleMuon2017E_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim17     ${datadir}/Run2017F/SingleMuon ${tgdir}/SingleMuon2017F &> ${log}/SingleMuon2017F_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim18     ${datadir}/Run2018A/SingleMuon ${tgdir}/SingleMuon2018A &> ${log}/SingleMuon2018A_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim18     ${datadir}/Run2018B/SingleMuon ${tgdir}/SingleMuon2018B &> ${log}/SingleMuon2018B_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim18     ${datadir}/Run2018C/SingleMuon ${tgdir}/SingleMuon2018C &> ${log}/SingleMuon2018C_skim.out
./skimnanoaod.py -F --split ${njobs} -Y skim18     ${datadir}/Run2018D/SingleMuon ${tgdir}/SingleMuon2018D &> ${log}/SingleMuon2018D_skim.out
