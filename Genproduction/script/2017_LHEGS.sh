#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc630
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_9_3_4/src ] ; then 
    echo release CMSSW_9_3_4 already exists
else
    scram p CMSSW CMSSW_9_3_4
fi
cd CMSSW_9_3_4/src
eval `scram runtime -sh`

#curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TOP-RunIIFall17wmLHEGS-00034 --retry 2 --create-dirs -o Configuration/GenProduction/python/TOP-RunIIFall17wmLHEGS-00034-fragment.py 
#[ -s Configuration/GenProduction/python/TOP-RunIIFall17wmLHEGS-00034-fragment.py ] || exit $?;

voms-proxy-init -voms cms
#git cms-addpkg Configuration/Generator
#git cms-addpkg GeneratorInterface/LHEInterface
cd Configuration
#git clone git@github.com:cms-sw/genproductions.git GenProduction
cd ..
rm -rf Configuration/GenProduction/python/ThirteenTeV/DelayedJets
cp ../../LQ_cmutau_cfg.py Configuration/GenProduction/python/

scram b
cd ../../
seed=$(($(date +%s) % 100 + 1))
cmsDriver.py Configuration/GenProduction/python/LQ_cmutau_cfg.py --fileout file:LQ_2017LHEGS_v1.root --mc --eventcontent RAWSIM,LHE --datatier GEN-SIM,LHE --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN,SIM --nThreads 8 --geometry DB:Extended --era Run2_2017 --python_filename LQ_2017LHEGS_v1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n 1000 || exit $? ; 
