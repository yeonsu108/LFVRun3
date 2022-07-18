#!/bin/bash
version=skim_LFVv8
mc16pre=/data1/common/skimmed_NanoAOD/$version/mc/16pre
mc16post=/data1/common/skimmed_NanoAOD/$version/mc/16post
mc17=/data1/common/skimmed_NanoAOD/$version/mc/17
mc18=/data1/common/skimmed_NanoAOD/$version/mc/18
json16=data/GoldenJSON/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt
json17=data/GoldenJSON/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt
json18=data/GoldenJSON/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt
# Syst : nom, jecup, jecdown, puup, pudown, btagup_jes, btagdown_jes
syst=nom
mkdir -p ${target}

# Test for processonefile.py
#./processonefile.py -Y 18 -S ${syst} --globaltag Summer19UL16APV_V7 /data1/common/skimmed_NanoAOD/skim_LFVv8/mc/18/TTTo2L2Nu/270000_019426EE-3D50-1249-B266-F6DBA0AFE3B5_analyzed.root test_process_mc_TTTo2L2Nu.root outputTree outputTree2 &> test_process_mc_TTTo2L2Nu.out

# Test for processnanoaod.py
# DATA
./processnanoaod_ST.py -A -Y 16post -S ${syst} --globaltag Summer19UL16_RunFGH_V7 -J ${json16} ./SingleMuon2016Fpost test_process_Run16postF_${syst}.root   &> test_process_Run16postF_${syst}.out &

# MC
./processnanoaod_ST.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ./ST_t-channel_top test_process_ST_t-channel_top_18_${syst}.root &> test_process_ST_t-channel_top_18_${syst}.out &
#./processnanoaod_ST.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ./DYJetsToLL_M-50_amcatnlo test_process_DYJetsToLL_M-50_amcatnlo_18_${syst}.root &> test_process_DYJetsToLL_M-50_amcatnlo_18_${syst}.out &
