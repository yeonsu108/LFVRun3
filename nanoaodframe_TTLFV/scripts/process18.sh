#!/bin/bash
version=skim_LFVv8
datapath=/data1/common/skimmed_NanoAOD/$version/data
mc18=/data1/common/skimmed_NanoAOD/$version/mc/18
# Sys : norm, jecup, jecdown, puup, pudown, btagup_jes, btagdown_jes
# btagup_lf, btagdown_lf, btagup_hf, btagdown_hf
syst=norm
target=feb_01_${syst} # Arbitrary folder name
jsonfile="data/GoldenJSON/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt"
mkdir -p "${target}"
# 18
./processnanoaod.py --allinone -Y 18 -S ${syst} --globaltag Summer19UL18_RunA_V5 --json="${jsonfile}" ${datapath}/SingleMuon2018A ${target}/Run18A_${syst}.root &> ${target}/Run18A_${syst}.out &
./processnanoaod.py --allinone -Y 18 -S ${syst} --globaltag Summer19UL18_RunB_V5 --json="${jsonfile}" ${datapath}/SingleMuon2018B ${target}/Run18B_${syst}.root &> ${target}/Run18B_${syst}.out &
./processnanoaod.py --allinone -Y 18 -S ${syst} --globaltag Summer19UL18_RunC_V5 --json="${jsonfile}" ${datapath}/SingleMuon2018C ${target}/Run18C_${syst}.root &> ${target}/Run18C_${syst}.out &
./processnanoaod.py --allinone -Y 18 -S ${syst} --globaltag Summer19UL18_RunD_V5 --json="${jsonfile}" ${datapath}/SingleMuon2018D/000 ${target}/Run18D_${syst}_1.root &> ${target}/Run18D_${syst}_1.out &
./processnanoaod.py --allinone -Y 18 -S ${syst} --globaltag Summer19UL18_RunD_V5 --json="${jsonfile}" ${datapath}/SingleMuon2018D/049 ${target}/Run18D_${syst}_2.root &> ${target}/Run18D_${syst}_2.out &
./processnanoaod.py --allinone -Y 18 -S ${syst} --globaltag Summer19UL18_RunD_V5 --json="${jsonfile}" ${datapath}/SingleMuon2018D/098 ${target}/Run18D_${syst}_3.root &> ${target}/Run18D_${syst}_3.out &
./processnanoaod.py --allinone -Y 18 -S ${syst} --globaltag Summer19UL18_RunD_V5 --json="${jsonfile}" ${datapath}/SingleMuon2018D/147 ${target}/Run18D_${syst}_4.root &> ${target}/Run18D_${syst}_4.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/DYJetsToLL_M-10to50 ${target}/DYJetsToLL_M-10to50_18_${syst}.root &> ${target}/DYJetsToLL_M-10to50_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/DYJetsToLL_M-50_amcatnlo ${target}/DYJetsToLL_M-50_amcatnlo_18_${syst}.root &> ${target}/DYJetsToLL_M-50_amcatnlo_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/DYJetsToLL_M-50_madgraph ${target}/DYJetsToLL_M-50_madgraph_18_${syst}.root &> ${target}/DYJetsToLL_M-50_madgraph_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/ST_t-channel_antitop ${target}/ST_t-channel_antitop_18_${syst}.root &> ${target}/ST_t-channel_antitop_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/ST_t-channel_top ${target}/ST_t-channel_top_18_${syst}.root &> ${target}/ST_t-channel_top_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/ST_tW_antitop ${target}/ST_tW_antitop_18_${syst}.root &> ${target}/ST_tW_antitop_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/ST_tW_top ${target}/ST_tW_top_18_${syst}.root &> ${target}/ST_tW_top_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/TTTo2L2Nu ${target}/TTTo2L2Nu_18_${syst}.root &> ${target}/TTTo2L2Nu_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/TTToHadronic ${target}/TTToHadronic_18_${syst}.root &> ${target}/TTToHadronic_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/TTToSemiLeptonic/000 ${target}/TTToSemiLeptonic_18_${syst}_1.root &> ${target}/TTToSemiLeptonic_18_${syst}_1.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/TTToSemiLeptonic/155 ${target}/TTToSemiLeptonic_18_${syst}_2.root &> ${target}/TTToSemiLeptonic_18_${syst}_2.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/TTToSemiLeptonic/310 ${target}/TTToSemiLeptonic_18_${syst}_3.root &> ${target}/TTToSemiLeptonic_18_${syst}_3.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/TTWJetsToLNu ${target}/TTWJetsToLNu_18_${syst}.root &> ${target}/TTWJetsToLNu_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/TTWJetsToQQ ${target}/TTWJetsToQQ_18_${syst}.root &> ${target}/TTWJetsToQQ_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/TTZToLLNuNu ${target}/TTZToLLNuNu_18_${syst}.root &> ${target}/TTZToLLNuNu_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/TTZToQQ ${target}/TTZToQQ_18_${syst}.root &> ${target}/TTZToQQ_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/WJetsToLNu_HT-0To100 ${target}/WJetsToLNu_HT-0To100_18_${syst}.root &> ${target}/WJetsToLNu_HT-0To100_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/WJetsToLNu_HT-100To200 ${target}/WJetsToLNu_HT-100To200_18_${syst}.root &> ${target}/WJetsToLNu_HT-100To200_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/WJetsToLNu_HT-200To400 ${target}/WJetsToLNu_HT-200To400_18_${syst}.root &> ${target}/WJetsToLNu_HT-200To400_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/WJetsToLNu_HT-400To600 ${target}/WJetsToLNu_HT-400To600_18_${syst}.root &> ${target}/WJetsToLNu_HT-400To600_18_${syst}.out &
#sleep 20m
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/WJetsToLNu_HT-600To800 ${target}/WJetsToLNu_HT-600To800_18_${syst}.root &> ${target}/WJetsToLNu_HT-600To800_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/WJetsToLNu_HT-800To1200 ${target}/WJetsToLNu_HT-800To1200_18_${syst}.root &> ${target}/WJetsToLNu_HT-800To1200_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/WJetsToLNu_HT-1200To2500 ${target}/WJetsToLNu_HT-1200To2500_18_${syst}.root &> ${target}/WJetsToLNu_HT-1200To2500_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/WJetsToLNu_HT-2500ToInf ${target}/WJetsToLNu_HT-2500ToInf_18_${syst}.root &> ${target}/WJetsToLNu_HT-2500ToInf_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/WW ${target}/WW_18_${syst}.root &> ${target}/WW_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/WZ ${target}/WZ_18_${syst}.root &> ${target}/WZ_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/ZZ ${target}/ZZ_18_${syst}.root &> ${target}/ZZ_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-15To20_MuEnrichedPt5 ${target}/QCD_Pt-15To20_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-15To20_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-20To30_MuEnrichedPt5 ${target}/QCD_Pt-20To30_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-20To30_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-30To50_MuEnrichedPt5 ${target}/QCD_Pt-30To50_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-30To50_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-50To80_MuEnrichedPt5 ${target}/QCD_Pt-50To80_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-50To80_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-80To120_MuEnrichedPt5 ${target}/QCD_Pt-80To120_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-80To120_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-120To170_MuEnrichedPt5 ${target}/QCD_Pt-120To170_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-120To170_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-170To300_MuEnrichedPt5 ${target}/QCD_Pt-170To300_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-170To300_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-300To470_MuEnrichedPt5 ${target}/QCD_Pt-300To470_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-300To470_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-470To600_MuEnrichedPt5 ${target}/QCD_Pt-470To600_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-470To600_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-600To800_MuEnrichedPt5 ${target}/QCD_Pt-600To800_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-600To800_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-800To1000_MuEnrichedPt5 ${target}/QCD_Pt-800To1000_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-800To1000_MuEnrichedPt5_18_${syst}.out &
#./processnanoaod.py -A -Y 18 -S ${syst} --globaltag Summer19UL18_V5 ${mc18}/QCD_Pt-1000_MuEnrichedPt5 ${target}/QCD_Pt-1000_MuEnrichedPt5_18_${syst}.root &> ${target}/QCD_Pt-1000_MuEnrichedPt5_18_${syst}.out &
