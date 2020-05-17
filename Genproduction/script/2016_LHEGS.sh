#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc481
source /cvmfs/cms.cern.ch/cmsset_default.sh
if [ -r CMSSW_7_1_38/src ] ; then 
 echo release CMSSW_7_1_38 already exists
else
scram p CMSSW CMSSW_7_1_38
fi
cd CMSSW_7_1_38/src
eval `scram runtime -sh`

#curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TOP-RunIISummer15wmLHEGS-00420 --retry 2 --create-dirs -o Configuration/GenProduction/python/TOP-RunIISummer15wmLHEGS-00420-fragment.py 
#[ -s Configuration/GenProduction/python/TOP-RunIISummer15wmLHEGS-00420-fragment.py ] || exit $?;

voms-proxy-init -voms cms
git cms-addpkg Configuration/Generator
git cms-addpkg GeneratorInterface/LHEInterface
cd Configuration
git clone git@github.com:cms-sw/genproductions.git GenProduction
cd ..
rm -rf Configuration/GenProduction/python/ThirteenTeV/DelayedJets
cp ../../../LQ_cmutau_cfg.py Configuration/GenProduction/python/

scram b -j 10
cd ../../
seed=$(($(date +%s) % 100 + 1))
cmsDriver.py Configuration/GenProduction/python/LQ_cmutau_cfg.py --fileout file:LQ_2016LHEGS_v1.root --mc --eventcontent RAWSIM,LHE --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM,LHE --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step LHE,GEN,SIM --magField 38T_PostLS1 --python_filename LQ_2016LHEGS_v1_cfg.py --no_exec --customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed="int(${seed})" -n 1000 || exit $? ;
cp LQ_2016LHEGS_v1_cfg.py CMSSW_7_1_38/src/
cd CMSSW_7_1_38/src
