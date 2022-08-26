#!/bin/bash
version=skim_LFVv8
inpath=/data1/common/skimmed_NanoAOD/$version/data
# syst
# nom, jecup, jecdown, puup, pudown, btagup_jes, btagdown_jes
# btagup_hf, btagdown_hf, btagup_lf, btagdown_lf
# btag
# 'Absolute', 'Absolute_2018', 'BBEC1', 'BBEC1_2018', 'EC2', 'EC2_2018', 'FlavorQCD', 'HF', 'HF_2018', 'RelativeBal', 'RelativeSample_2018'
label=aug22     # Arbitrary strings
ana=$1          # or ttlfv
syst=nom
target=${label}_${ana}/${syst} # Arbitrary folder name
mkdir -p ${target}
json16=data/GoldenJSON/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt
json17=data/GoldenJSON/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt
json18=data/GoldenJSON/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt
./processnanoaod.py --analyzer ${ana} -A -Y 16pre -S ${syst} --globaltag Summer19UL16APV_RunBCD_V7 -J ${json16} ${inpath}/SingleMuon2016B2    ${target}/Run16preB2_${syst}.root   &> ${target}/Run16preB2_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 16pre -S ${syst} --globaltag Summer19UL16APV_RunBCD_V7 -J ${json16} ${inpath}/SingleMuon2016C     ${target}/Run16preC_${syst}.root    &> ${target}/Run16preC_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 16pre -S ${syst} --globaltag Summer19UL16APV_RunBCD_V7 -J ${json16} ${inpath}/SingleMuon2016D     ${target}/Run16preD_${syst}.root    &> ${target}/Run16preD_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 16pre -S ${syst} --globaltag Summer19UL16APV_RunEF_V7  -J ${json16} ${inpath}/SingleMuon2016E     ${target}/Run16preE_${syst}.root    &> ${target}/Run16preE_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 16pre -S ${syst} --globaltag Summer19UL16APV_RunEF_V7  -J ${json16} ${inpath}/SingleMuon2016Fpre  ${target}/Run16preF_${syst}.root    &> ${target}/Run16preF_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 16post -S ${syst} --globaltag Summer19UL16_RunFGH_V7   -J ${json16} ${inpath}/SingleMuon2016Fpost ${target}/Run16postF_${syst}.root   &> ${target}/Run16postF_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 16post -S ${syst} --globaltag Summer19UL16_RunFGH_V7   -J ${json16} ${inpath}/SingleMuon2016G     ${target}/Run16postG_${syst}.root   &> ${target}/Run16postG_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 16post -S ${syst} --globaltag Summer19UL16_RunFGH_V7   -J ${json16} ${inpath}/SingleMuon2016H     ${target}/Run16postH_${syst}.root   &> ${target}/Run16postH_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 17 -S ${syst} --globaltag Summer19UL17_RunB_V5         -J ${json17} ${inpath}/SingleMuon2017B     ${target}/Run17B_${syst}.root       &> ${target}/Run17B_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 17 -S ${syst} --globaltag Summer19UL17_RunC_V5         -J ${json17} ${inpath}/SingleMuon2017C     ${target}/Run17C_${syst}.root       &> ${target}/Run17C_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 17 -S ${syst} --globaltag Summer19UL17_RunD_V5         -J ${json17} ${inpath}/SingleMuon2017D     ${target}/Run17D_${syst}.root       &> ${target}/Run17D_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 17 -S ${syst} --globaltag Summer19UL17_RunE_V5         -J ${json17} ${inpath}/SingleMuon2017E     ${target}/Run17E_${syst}.root       &> ${target}/Run17E_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 17 -S ${syst} --globaltag Summer19UL17_RunF_V5         -J ${json17} ${inpath}/SingleMuon2017F/000 ${target}/Run17F_${syst}_1.root     &> ${target}/Run17F_${syst}_1.out &
./processnanoaod.py --analyzer ${ana} -A -Y 17 -S ${syst} --globaltag Summer19UL17_RunF_V5         -J ${json17} ${inpath}/SingleMuon2017F/058 ${target}/Run17F_${syst}_2.root     &> ${target}/Run17F_${syst}_2.out &
./processnanoaod.py --analyzer ${ana} -A -Y 17 -S ${syst} --globaltag Summer19UL17_RunF_V5         -J ${json17} ${inpath}/SingleMuon2017F/116 ${target}/Run17F_${syst}_3.root     &> ${target}/Run17F_${syst}_3.out &
./processnanoaod.py --analyzer ${ana} -A -Y 18 -S ${syst} --globaltag Summer19UL18_RunA_V5         -J ${json18} ${inpath}/SingleMuon2018A     ${target}/Run18A_${syst}.root       &> ${target}/Run18A_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 18 -S ${syst} --globaltag Summer19UL18_RunB_V5         -J ${json18} ${inpath}/SingleMuon2018B     ${target}/Run18B_${syst}.root       &> ${target}/Run18B_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 18 -S ${syst} --globaltag Summer19UL18_RunC_V5         -J ${json18} ${inpath}/SingleMuon2018C     ${target}/Run18C_${syst}.root       &> ${target}/Run18C_${syst}.out &
./processnanoaod.py --analyzer ${ana} -A -Y 18 -S ${syst} --globaltag Summer19UL18_RunD_V5         -J ${json18} ${inpath}/SingleMuon2018D/000 ${target}/Run18D_${syst}_1.root     &> ${target}/Run18D_${syst}_1.out &
./processnanoaod.py --analyzer ${ana} -A -Y 18 -S ${syst} --globaltag Summer19UL18_RunD_V5         -J ${json18} ${inpath}/SingleMuon2018D/049 ${target}/Run18D_${syst}_2.root     &> ${target}/Run18D_${syst}_2.out &
./processnanoaod.py --analyzer ${ana} -A -Y 18 -S ${syst} --globaltag Summer19UL18_RunD_V5         -J ${json18} ${inpath}/SingleMuon2018D/098 ${target}/Run18D_${syst}_3.root     &> ${target}/Run18D_${syst}_3.out &
./processnanoaod.py --analyzer ${ana} -A -Y 18 -S ${syst} --globaltag Summer19UL18_RunD_V5         -J ${json18} ${inpath}/SingleMuon2018D/147 ${target}/Run18D_${syst}_4.root     &> ${target}/Run18D_${syst}_4.out &
