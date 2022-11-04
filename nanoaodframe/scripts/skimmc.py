import os, sys
import subprocess

version = sys.argv[1] #skim_test
year = sys.argv[2]

workdir = os.getcwd()
tgdir = '/data1/common/skimmed_NanoAOD/' + version + '/DATAMC/' + year
log = '/data1/common/skimmed_NanoAOD/' + version + '/log/' + year 

os.makedirs(tgdir.replace('DATAMC', 'data'), exist_ok=True)
os.makedirs(tgdir.replace('DATAMC', 'mc'), exist_ok=True)
os.makedirs(log, exist_ok=True)

for fn in os.listdir("data/dataset/v8UL_20" + year):
    if 'json' in fn: continue
    fname = fn.lstrip('dataset_').rstrip('.txt')
    if not 'SingleMuon2016B' in fname: continue
    with open(os.path.join("data/dataset/v8UL_20" + year, fn), 'r') as f:
        for line in f.readlines():
            if line.startswith('#'): continue
            lsplit = line.rstrip('\n').split('/')
            if any('Run201' in l for l in lsplit):
                outputdir = tgdir.replace('DATAMC', 'data')
            else:
                outputdir = tgdir.replace('DATAMC', 'mc')
            os.makedirs(os.path.join(outputdir, fname), exist_ok=True)
            logdir = os.path.join(log, fname)
            os.makedirs(logdir, exist_ok=True)
            print("sbatch scripts/job_slurm.sh " + "skim" + year + " " + line.rstrip('\n') + " " + os.path.join(outputdir, fname) + " " + lsplit[-2] + '_' + lsplit[-1].replace('.root', '_analyzed.root') + " Events outputTree " + workdir + " " + logdir + " " + fname)
            subprocess.call(["sbatch scripts/job_slurm.sh " + "skim" + year + " " + line.rstrip('\n') + " " + os.path.join(outputdir, fname) + " " + lsplit[-2] + '_' + lsplit[-1].replace('.root', '_analyzed.root') + " Events outputTree " + workdir + " " + logdir + " " + fname], shell=True)
