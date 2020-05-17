#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_4_7/src ] ; then 
    echo release CMSSW_9_4_7 already exists
else
    scram p CMSSW CMSSW_9_4_7
fi
cd CMSSW_9_4_7/src
eval `scram runtime -sh`
voms-proxy-init -voms cms

scram b
cd ../../
cmsDriver.py step1 --filein file:LQ_2017LHEGS_v1.root --fileout file:LQ_2017_step1.root  --pileup_input "dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MCv2_correctPU_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW" --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v11 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename LQ_2017_step1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 || exit $? ; 

cmsDriver.py step2 --filein file:LQ_2017_step1.root --fileout file:LQ_2017_step2.root --mc --eventcontent AODSIM --runUnscheduled --datatier AODSIM --conditions 94X_mc2017_realistic_v11 --step RAW2DIGI,RECO,RECOSIM,EI --nThreads 8 --era Run2_2017 --python_filename LQ_2017_step2_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751 || exit $? ; 
