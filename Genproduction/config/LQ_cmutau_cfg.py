import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('LQ_cmutau_slc6_amd64_gcc700_CMSSW_10_2_19_tarball.tar.xz'),
    #args = cms.vstring('root://cms-xrdr.sdfarm.kr:1094//store/user/ljw1015/LQ_cmutau_slc6_amd64_gcc700_CMSSW_10_2_19_tarball.tar.xz'),
    #args = cms.vstring('root://eosuser.cern.ch:/eos/user/j/jolim/private/LQ_cmutau_slc6_amd64_gcc700_CMSSW_10_2_19_tarball.tar.xz'),
    #args = cms.vstring('root://eosuser.cern.ch//eos/user/j/jolim/public/LQ_cmutau_slc6_amd64_gcc700_CMSSW_10_2_19_tarball'),
    nEvents = cms.untracked.uint32(100),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    )
    )
)
