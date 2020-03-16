# Single Muon
create-batch bash ntuple.sh listmaker/List/data_Run2016_SingleMuon.txt 1 --jobName data_Run2016_SingleMuon --nJobs 431 --transferFiles output.root
create-batch bash ntuple.sh listmaker/List/data_Run2017_SingleMuon.txt 1 --jobName data_Run2017_SingleMuon --nJobs 454 --transferFiles output.root
create-batch bash ntuple.sh listmaker/List/data_Run2018_SingleMuon.txt 1 --jobName data_Run2018_SingleMuon --nJobs 818 --transferFiles output.root

# Tau
#create-batch bash ntuple.sh listmaker/List/data_Run2016_Tau.txt 1 --jobName data_Run2016_Tau_1 --nJobs 248 --transferFiles output.root
#create-batch bash ntuple.sh listmaker/List/data_Run2017_Tau.txt 1 --jobName data_Run2017_Tau_1 --nJobs 196 --transferFiles output.root
#create-batch bash ntuple.sh listmaker/List/data_Run2018_Tau.txt 1 --jobName data_Run2018_Tau_1 --nJobs 221 --transferFiles output.root
#create-batch bash ntuple.sh listmaker/List/data_Run2018_Tau.txt 1 --jobName test_job --nJobs 1 --transferFiles output.root

