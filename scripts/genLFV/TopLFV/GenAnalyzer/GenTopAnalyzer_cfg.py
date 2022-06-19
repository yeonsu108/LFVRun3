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
            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TCMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_ST_TCMuTau_Scalar_MINI/210427_010007/0000/LFV_ST_TCMuTau_Scalar_MINI_Apr2021_A_6.root'))
#            'file:root://cms-xrd-global.cern.ch//store/mc/RunIISummer19UL18RECO/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/260001/0E08047F-7F0C-4E4A-AF4F-AD22AEC515A9.root'))
#            'file:root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18DRPremix/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/00000/004D4C45-3D10-074E-A176-EC31BBEF5DBB.root'))
#            'file:root://cms-xrd-global.cern.ch//store/mc/RunIISummer19UL18RECO/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/AODSIM/106X_upgrade2018_realistic_v11_L1v1-v2/260002/BB5E5DE2-DEA7-1442-A17B-2DFD68D46F94.root'))
#            'file:root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18DRPremix/TTJets_TuneCP5_13TeV-madgraphMLM-pythia8/AODSIM/102X_upgrade2018_realistic_v15-v1/90000/FFF6B4CB-0D80-C84A-AD75-1CA30FCBD8DE.root'))

process.genana = cms.EDAnalyzer('GenTopAnalyzer'
                        ,genParticleLabel = cms.untracked.InputTag('prunedGenParticles'))

process.TFileService = cms.Service("TFileService"
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Clu_2018_GenAna_v2.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Ceu_2018_GenAna_v2.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Cqe_2018_GenAna_v2.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Clequ1_2018_GenAna_v2.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Clequ3_2018_GenAna_v2.root'))
#                        ,fileName = cms.string('LFV_TT_to_cmutau_Clq_2018_GenAna_v2.root'))
                        ,fileName = cms.string('LFV_ST_TCMuTau_Scalar_1.root'))
#                        ,fileName = cms.string('LQ_TT_to_cmutau_2018_GenAna_v2.root'))
#                       ,fileName = cms.string('SM_TTToSemiLeptonic_2018_GenAna_v2.root'))
#                       ,fileName = cms.string('SM_TTToDiLeptonic_2018_GenAna_v2.root'))

process.p = cms.Path(process.genana)
