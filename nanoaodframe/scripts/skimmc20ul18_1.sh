#!/bin/bash
#### SETTINGS ####
version=skim_LFVv8
njobs=25

#### PATHs ####
mcdir20ul18=/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL18NanoAODv2
tgdir18=/data1/common/skimmed_NanoAOD/${version}/mc/18
logdir=/data1/common/skimmed_NanoAOD/${version}/log
mkdir -p ${tgdir}
mkdir -p ${logdir}

# 18
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-15To20_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-15To20_MuEnrichedPt5 &> ${logdir}/QCD_Pt-15To20_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-20To30_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-20To30_MuEnrichedPt5 &> ${logdir}/QCD_Pt-20To30_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-30To50_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-30To50_MuEnrichedPt5 &> ${logdir}/QCD_Pt-30To50_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-50To80_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-50To80_MuEnrichedPt5 &> ${logdir}/QCD_Pt-50To80_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-80To120_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-80To120_MuEnrichedPt5 &> ${logdir}/QCD_Pt-80To120_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-120To170_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-120To170_MuEnrichedPt5 &> ${logdir}/QCD_Pt-120To170_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-170To300_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-170To300_MuEnrichedPt5 &> ${logdir}/QCD_Pt-170To300_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-300To470_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-300t470_MuEnrichedPt5 &> ${logdir}/QCD_Pt-300To470_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-470To600_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-470To600_MuEnrichedPt5 &> ${logdir}/QCD_Pt-470To600_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-600To800_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-600To800_MuEnrichedPt5 &> ${logdir}/QCD_Pt-600To800_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-800To1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-800To1000_MuEnrichedPt5 &> ${logdir}/QCD_Pt-800To1000_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/QCD_Pt-1000_MuEnrichedPt5_TuneCP5_13TeV-pythia8 ${tgdir18}/QCD_Pt-1000_MuEnrichedPt5 &> ${logdir}/QCD_Pt-1000_MuEnrichedPt5_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir18}/DYJetsToLL_M-10to50 &> ${logdir}/DYJetsToLL_M-10to50_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8 ${tgdir18}/DYJetsToLL_M-50_amcatnlo  &> ${logdir}/DYJetsToLL_M-50_amcatnlo_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir18}/DYJetsToLL_M-50_madgraph &> ${logdir}/DYJetsToLL_M-50_madgraph_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8 ${tgdir18}/ST_t-channel_antitop &> ${logdir}/ST_t-channel_antitop_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8 ${tgdir18}/ST_t-channel_top &> ${logdir}/ST_t-channel_top_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8 ${tgdir18}/ST_tW_antitop &> ${logdir}/ST_tW_antitop_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8 ${tgdir18}/ST_tW_top &> ${logdir}/ST_tW_top_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8 ${tgdir18}/TTTo2L2Nu &> ${logdir}/TTTo2L2Nu_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/TTToHadronic_TuneCP5_13TeV-powheg-pythia8 ${tgdir18}/TTToHadronic &> ${logdir}/TTToHadronic_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8 ${tgdir18}/TTToSemiLeptonic &> ${logdir}/TTToSemiLeptonic_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8 ${tgdir18}/TTWJetsToLNu &> ${logdir}/TTWJetsToLNu_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8 ${tgdir18}/TTWJetsToQQ &> ${logdir}/TTWJetsToQQ_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8 ${tgdir18}/TTZToLLNuNu &> ${logdir}/TTZToLLNuNu_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8 ${tgdir18}/TTZToQQ &> ${logdir}/TTZToQQ_skim18.out
#./skimnanoaod.py -F --split ${njobs} -Y wjetskim18 ${mcdir20ul18}/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir18}/WJetsToLNu_HT-0To100 &> ${logdir}/WJetsToLNu_HT-0To100_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir18}/WJetsToLNu_HT-100To200 &> ${logdir}/WJetsToLNu_HT-100To200_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir18}/WJetsToLNu_HT-200To400 &> ${logdir}/WJetsToLNu_HT-200To400_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir18}/WJetsToLNu_HT-400To600 &> ${logdir}/WJetsToLNu_HT-400To600_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir18}/WJetsToLNu_HT-600To800 &> ${logdir}/WJetsToLNu_HT-600To800_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir18}/WJetsToLNu_HT-800To1200 &> ${logdir}/WJetsToLNu_HT-800To1200_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir18}/WJetsToLNu_HT-1200To2500 &> ${logdir}/WJetsToLNu_HT-1200To2500_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8 ${tgdir18}/WJetsToLNu_HT-2500ToInf &> ${logdir}/WJetsToLNu_HT-2500ToInf_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/WW_TuneCP5_13TeV-pythia8 ${tgdir18}/WW &> ${logdir}/WW_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/WZ_TuneCP5_13TeV-pythia8 ${tgdir18}/WZ &> ${logdir}/WZ_skim18.out
./skimnanoaod.py -F --split ${njobs} -Y skim18 ${mcdir20ul18}/ZZ_TuneCP5_13TeV-pythia8 ${tgdir18}/ZZ &> ${logdir}/ZZ_skim18.out

#./skimnanoaod.py -F --split ${njobs} -Y skim16post ${mcdir20ul16post}/ ${tgdir16post}/ &> ${logdir}/_skim16post.out
