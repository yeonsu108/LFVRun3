# ntuplemaker
Purpose : Making flat ntuples from NanoAOD rootfiles

## ntuplemaker.C
Making ntuples with inputfile argument. Event selections with RDataFrame are applied.

```
*Usage*
root -l ntuplemaker.C'("inputfile.root")'
```

## ~~ntuplemaker.py~~ (out of date)
python version of ntuplemaker.C

## ntuple.sh
Configure file for condor batch job.   
From the filelist.txt file, get inputfile directory one by one and take it as an argument of **ntuplemaker.C**

## condor.sh
**ntuple.sh** is a configure file of "create-batch" command.   
And **condor.sh** runs "create-batch".
```
*Usage*
source condor.sh

*create-batch for ntuplemaker.C condor jobs*
create-batch bash ntuple.sh listmaker/List/data_Run2016_SingleMuon.txt 1 --jobName data_Run2016_SingleMuon --nJobs 431 --transferFiles output.root
```
Change ".txt" file which is filelist, jobName, nJobs (lines in filelist, one job per one inputfile).

## histmaker.py
Making histogram from ntuple.
```
*Usage*
python histmaker.py input_ntuple.root
```
