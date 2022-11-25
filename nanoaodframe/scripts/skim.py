import os, sys
from subprocess import call

version = sys.argv[1] #skim_test
year = sys.argv[2]
if len(sys.argv) > 3:
    dataOrMC = sys.argv[3] #'data' or 'mc'

workdir = os.getcwd()
tgdir = '/data1/common/skimmed_NanoAOD/' + version + '/DATAMC/' + year
log = '/data1/common/skimmed_NanoAOD/' + version + '/log/' + year 

os.makedirs(tgdir.replace('DATAMC', 'data'), exist_ok=True)
os.makedirs(tgdir.replace('DATAMC', 'mc'), exist_ok=True)
os.makedirs(log, exist_ok=True)

for fn in os.listdir("data/dataset/v8UL_" + year):
    if 'json' in fn: continue
    fname = fn.lstrip('dataset_').rstrip('.txt')
    test_list = []
    #test_list = ['TTToSemiLeptonic']
    if len(test_list) > 0:
        if not any(i in fname for i in test_list): continue
    if len(sys.argv) > 3:
        if dataOrMC == 'data':
            if '201' not in fname: continue
        elif dataOrMC == 'mc':
            if '201' in fname: continue

    with open(os.path.join("data/dataset/v8UL_" + year, fn), 'r') as f:
        for line in f.readlines():
            if line.startswith('#'): continue

            infile = line.rstrip('\n') 
            lsplit = infile.split('/')
            dirNum = lsplit[-2]
            rootName = lsplit[-1]

            if any('Run201' in l for l in lsplit):
                outputdir = tgdir.replace('DATAMC', 'data')
            else:
                outputdir = tgdir.replace('DATAMC', 'mc')

            os.makedirs(os.path.join(outputdir, fname), exist_ok=True)
            logdir = os.path.join(log, fname)
            os.makedirs(logdir, exist_ok=True)

            runString = "sbatch scripts/job_slurm_skim.sh " + year + " " + infile + " " + os.path.join(outputdir, fname) + " " + dirNum + '_' + rootName + " " + workdir + " " + logdir

            print(runString)
            #call([runString], shell=True)
