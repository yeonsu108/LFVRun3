from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'LQ_2018LHEGS'
config.General.workArea = 'crab_LQ_2018'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'LQ_2018LHEGS_v1_cfg.py'

config.section_("Data")
config.Data.outputPrimaryDataset = 'LQ_2018'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 200  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'LQ_2018LHEGS'

config.section_("Site")
config.Site.storageSite = 'T2_KR_KISTI'
