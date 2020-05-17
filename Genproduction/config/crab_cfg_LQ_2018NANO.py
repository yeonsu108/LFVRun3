from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'LQ_2018NANO'
config.General.workArea = 'crab_LQ_2018'
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'LQ_2018_nano_cfg.py'
config.JobType.maxMemoryMB = 5000
config.JobType.numCores = 2

config.section_("Data")
config.Data.inputDataset = '/LQ_2018/jolim-LQ_2018MINI-8c47adb282cd21f1ab3845923e388b14/USER'
config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader/'
config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 1000
NJOBS = 50  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.ignoreLocality = True
config.Data.publication = True
config.Data.outputDatasetTag = 'LQ_2018NANO'

config.section_("Site")
config.Site.whitelist = ['T2_KR_KISTI']
config.Site.storageSite = 'T2_KR_KISTI'
