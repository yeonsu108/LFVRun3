import FWCore.ParameterSet.Config as cms

process = cms.Process("TopLFV")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
            'file:/cms/scratch/jolim/LFV/LFV_TT_to_cmutau_Clu_2018_LHEGS.root'))
#            'file:/cms/scratch/jolim/LFV/LFV_TT_to_cmutau_Ceu_2018_LHEGS.root'))
#            'file:/cms/scratch/jolim/LFV/LFV_TT_to_cmutau_Cqe_2018_LHEGS.root'))
#            'file:/cms/scratch/jolim/LFV/LFV_TT_to_cmutau_Clequ1_2018_LHEGS.root'))
#            'file:/cms/scratch/jolim/LFV/LFV_TT_to_cmutau_Clequ3_2018_LHEGS.root'))

process.genana = cms.EDAnalyzer('GenAnalyzer'
                        ,genParticleLabel = cms.untracked.InputTag('genParticles'))

process.TFileService = cms.Service("TFileService"
                        ,fileName = cms.string('LFV_TT_to_cmutau_Clu_2018_GenAna.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Ceu_2018_GenAna.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Cqe_2018_GenAna.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Clequ1_2018_GenAna.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Clequ3_2018_GenAna.root'))

process.p = cms.Path(process.genana)
