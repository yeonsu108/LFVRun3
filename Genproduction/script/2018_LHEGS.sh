#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_10_2_3/src ] ; then 
    echo release CMSSW_10_2_3 already exists
else
    scram p CMSSW CMSSW_10_2_3
fi
cd CMSSW_10_2_3/src
eval `scram runtime -sh`

#curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TOP-RunIIFall18wmLHEGS-00001 --retry 2 --create-dirs -o Configuration/GenProduction/python/TOP-RunIIFall18wmLHEGS-00001-fragment.py 
#[ -s Configuration/GenProduction/python/TOP-RunIIFall18wmLHEGS-00001-fragment.py ] || exit $?;

voms-proxy-init -voms cms
git cms-addpkg Configuration/Generator
git cms-addpkg GeneratorInterface/LHEInterface
cd Configuration
git clone git@github.com:cms-sw/genproductions.git GenProduction
cd ..
rm -rf Configuration/GenProduction/python/ThirteenTeV/DelayedJets
cp ../../LQ_cmutau_cfg.py Configuration/GenProduction/python/

scram b
cd ../../
seed=$(($(date +%s) % 100 + 1))
cmsDriver.py Configuration/GenProduction/python/LQ_cmutau_cfg.py --fileout file:LQ_2018LHEGS_v1.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 102X_upgrade2018_realistic_v11 --beamspot Realistic25ns13TeVEarly2018Collision --step LHE,GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2018 --python_filename LQ_2018LHEGS_v1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n 10000 || exit $? ; 

