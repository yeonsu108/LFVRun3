import FWCore.ParameterSet.Config as cms

process = cms.Process("TopLFV")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
#            'file:/cms/scratch/jolim/LFV_v2/LFV_TT_to_cmutau_Clu_2018_LHEGS.root'))
#            'file:/cms/scratch/jolim/LFV_v2/LFV_TT_to_cmutau_Ceu_2018_LHEGS.root'))
#            'file:/cms/scratch/jolim/LFV_v2/LFV_TT_to_cmutau_Cqe_2018_LHEGS.root'))
#            'file:/cms/scratch/jolim/LFV_v2/LFV_TT_to_cmutau_Clequ1_2018_LHEGS.root'))
#            'file:/cms/scratch/jolim/LFV_v2/LFV_TT_to_cmutau_Clequ3_2018_LHEGS.root'))
#            'file:/cms/scratch/jolim/LFV_v2/LFV_TT_to_cmutau_Clq_2018_LHEGS.root'))
#            'file:/T2_KR_KISTI/store/user/jolim/LQ_2018/LQ_2018AOD_B1/200717_044723/0000/LQ_2018_step2_1.root'))
#            'file:root://cms-xrd-global.cern.ch//store/mc/RunIISummer19UL18RECO/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/260001/0E08047F-7F0C-4E4A-AF4F-AD22AEC515A9.root'))
            'file:root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18DRPremix/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/20000/8811A358-A4AE-0940-BFF3-CE094D1B67E8.root'))

process.genana = cms.EDAnalyzer('GenAnalyzer'
                        ,genParticleLabel = cms.untracked.InputTag('genParticles'))

process.TFileService = cms.Service("TFileService"
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Clu_2018_GenAna_v1.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Ceu_2018_GenAna_v1.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Cqe_2018_GenAna_v1.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Clequ1_2018_GenAna_v1.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Clequ3_2018_GenAna_v1.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Clq_2018_GenAna_v1.root'))
#                        ,fileName = cms.string('LQ_TT_to_cmutau_2018_GenAna_v1.root'))
                        ,fileName = cms.string('SM_TTToSemiLeptonic_2018_GenAna_v1.root'))

process.p = cms.Path(process.genana)
