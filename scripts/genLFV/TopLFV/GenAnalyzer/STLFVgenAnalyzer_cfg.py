import FWCore.ParameterSet.Config as cms

process = cms.Process("TopLFV")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
        fileNames = cms.untracked.vstring(
#            # ST TCMuTau Scalar
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TCMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_ST_TCMuTau_Scalar_MINI/210427_010007/0000/LFV_ST_TCMuTau_Scalar_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TCMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_ST_TCMuTau_Scalar_MINI/210427_010007/0000/LFV_ST_TCMuTau_Scalar_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TCMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_ST_TCMuTau_Scalar_MINI/210427_010007/0000/LFV_ST_TCMuTau_Scalar_MINI_Apr2021_A_52.root'))

#            # ST TCMuTau Vector
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TCMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_ST_TCMuTau_Vector_MINI/210510_082153/0000/LFV_ST_TCMuTau_Vector_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TCMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_ST_TCMuTau_Vector_MINI/210510_082153/0000/LFV_ST_TCMuTau_Vector_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TCMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_ST_TCMuTau_Vector_MINI/210510_082153/0000/LFV_ST_TCMuTau_Vector_MINI_Apr2021_A_52.root'))

#            # ST TCMuTau Tensor
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TCMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_ST_TCMuTau_Tensor_MINI/210420_080119/0000/LFV_ST_TCMuTau_Tensor_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TCMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_ST_TCMuTau_Tensor_MINI/210420_080119/0000/LFV_ST_TCMuTau_Tensor_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TCMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_ST_TCMuTau_Tensor_MINI/210420_080119/0000/LFV_ST_TCMuTau_Tensor_MINI_Apr2021_A_52.root'))

#            # ST TUMuTau Scalar
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TUMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_ST_TUMuTau_Scalar_MINI/210510_081540/0000/LFV_ST_TUMuTau_Scalar_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TUMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_ST_TUMuTau_Scalar_MINI/210510_081540/0000/LFV_ST_TUMuTau_Scalar_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TUMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_ST_TUMuTau_Scalar_MINI/210510_081540/0000/LFV_ST_TUMuTau_Scalar_MINI_Apr2021_A_52.root'))

#            # ST TUMuTau Vector
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TUMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_ST_TUMuTau_Vector_MINI/210427_010111/0000/LFV_ST_TUMuTau_Vector_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TUMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_ST_TUMuTau_Vector_MINI/210427_010111/0000/LFV_ST_TUMuTau_Vector_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TUMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_ST_TUMuTau_Vector_MINI/210427_010111/0000/LFV_ST_TUMuTau_Vector_MINI_Apr2021_A_52.root'))

#            # ST TUMuTau Tensor
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TUMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_ST_TUMuTau_Tensor_MINI/210420_080229/0000/LFV_ST_TUMuTau_Tensor_MINI_Apr2021_A_2-50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TUMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_ST_TUMuTau_Tensor_MINI/210420_080229/0000/LFV_ST_TUMuTau_Tensor_MINI_Apr2021_A_2-51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_ST_TUMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_ST_TUMuTau_Tensor_MINI/210420_080229/0000/LFV_ST_TUMuTau_Tensor_MINI_Apr2021_A_2-52.root'))
#
#            # TT TCMuTau Scalar
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToCMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_TT_TToCMuTau_Scalar_MINI/210510_082911/0000/LFV_TT_TToCMuTau_Scalar_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToCMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_TT_TToCMuTau_Scalar_MINI/210510_082911/0000/LFV_TT_TToCMuTau_Scalar_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToCMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_TT_TToCMuTau_Scalar_MINI/210510_082911/0000/LFV_TT_TToCMuTau_Scalar_MINI_Apr2021_A_52.root')) 

#            # TT TCMuTau Vector
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToCMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_TT_TToCMuTau_Vector_MINI/210510_083034/0000/LFV_TT_TToCMuTau_Vector_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToCMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_TT_TToCMuTau_Vector_MINI/210510_083034/0000/LFV_TT_TToCMuTau_Vector_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToCMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_TT_TToCMuTau_Vector_MINI/210510_083034/0000/LFV_TT_TToCMuTau_Vector_MINI_Apr2021_A_52.root'))
#
#            # TT TCMuTau Tensor
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToCMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_TT_TToCMuTau_Tensor_MINI/210420_080330/0000/LFV_TT_TToCMuTau_Tensor_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToCMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_TT_TToCMuTau_Tensor_MINI/210420_080330/0000/LFV_TT_TToCMuTau_Tensor_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToCMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_TT_TToCMuTau_Tensor_MINI/210420_080330/0000/LFV_TT_TToCMuTau_Tensor_MINI_Apr2021_A_52.root'))

#            # TT TUMuTau Scalar
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToCMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_TT_TToCMuTau_Tensor_MINI/210420_080330/0000/LFV_TT_TToCMuTau_Tensor_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToUMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_TT_TToUMuTau_Scalar_MINI/210516_175503/0000/LFV_TT_TToUMuTau_Scalar_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToUMuTau_Scalar_RunIISummer20UL18-Apr2021_A/LFV_TT_TToUMuTau_Scalar_MINI/210516_175503/0000/LFV_TT_TToUMuTau_Scalar_MINI_Apr2021_A_52.root')) 
#
#            # TT TUMuTau Vector
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToUMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_TT_TToUMuTau_Vector_MINI/210427_063354/0000/LFV_TT_TToUMuTau_Vector_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToUMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_TT_TToUMuTau_Vector_MINI/210427_063354/0000/LFV_TT_TToUMuTau_Vector_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToUMuTau_Vector_RunIISummer20UL18-Apr2021_A/LFV_TT_TToUMuTau_Vector_MINI/210427_063354/0000/LFV_TT_TToUMuTau_Vector_MINI_Apr2021_A_52.root'))

            # TT TUMuTau Tensor
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToUMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_TT_TToUMuTau_Tensor_MINI/210510_082755/0000/LFV_TT_TToUMuTau_Tensor_MINI_Apr2021_A_50.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToUMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_TT_TToUMuTau_Tensor_MINI/210510_082755/0000/LFV_TT_TToUMuTau_Tensor_MINI_Apr2021_A_51.root',
#            'file:/T2_KR_KISTI/store/user/jolim/LFV_TT_TToUMuTau_Tensor_RunIISummer20UL18-Apr2021_A/LFV_TT_TToUMuTau_Tensor_MINI/210510_082755/0000/LFV_TT_TToUMuTau_Tensor_MINI_Apr2021_A_52.root'))

#            # SM TTbar
            'file:root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/00000/21B996BC-8CB3-1A40-ACE3-64DDECADDDE8.root',
            'file:root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/00000/25840049-8F8B-B449-8A69-57D711B71239.root',
            'file:root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/00000/27A87F71-7D93-D547-AD16-31084E549053.root',
            'file:root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/00000/2B6DCD9D-A589-0F48-91D5-06C355FFBDA1.root'))

process.genana = cms.EDAnalyzer('STLFVgenAnalyzer'
                        ,genParticleLabel = cms.untracked.InputTag('prunedGenParticles'))

process.TFileService = cms.Service("TFileService"
#                        ,fileName = cms.string('LFV_ST_TCMuTau_Scalar_V1.root'))
#                        ,fileName = cms.string('LFV_ST_TCMuTau_Vector_V1.root'))
#                        ,fileName = cms.string('LFV_ST_TCMuTau_Tensor_V1.root'))
#                        ,fileName = cms.string('LFV_ST_TUMuTau_Scalar_V1.root'))
#                        ,fileName = cms.string('LFV_ST_TUMuTau_Vector_V1.root'))
#                        ,fileName = cms.string('LFV_ST_TUMuTau_Tensor_V1.root'))
#                        ,fileName = cms.string('LFV_TT_TCMuTau_Scalar_V1.root'))
#                        ,fileName = cms.string('LFV_TT_TCMuTau_Vector_V1.root'))
#                        ,fileName = cms.string('LFV_TT_TCMuTau_Tensor_V1.root'))
#                        ,fileName = cms.string('LFV_TT_TUMuTau_Scalar_V1.root'))
#                        ,fileName = cms.string('LFV_TT_TUMuTau_Vector_V1.root'))
#                        ,fileName = cms.string('LFV_TT_TUMuTau_Tensor_V1.root'))
                        ,fileName = cms.string('SM_TTbar_dileptonic_V1.root'))

process.p = cms.Path(process.genana)
