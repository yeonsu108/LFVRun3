import os, sys
from subprocess import call

version = sys.argv[1] #folder under /data1/common/skimmed_NanoAOD/
output = sys.argv[2] #output folder in your working directory
year = sys.argv[3]
if len(sys.argv) > 4:
    dataOrMC = sys.argv[4] #'data' or 'mc'

workdir = os.getcwd()
indir = os.path.join('/data1/common/skimmed_NanoAOD/', version)
tgdir = os.path.join(workdir, output, year, 'temp')
log = os.path.join(workdir, output, year, 'log')
syst = "all" #placeholder for sf uncs.

os.makedirs(tgdir, exist_ok=True)
os.makedirs(log, exist_ok=True)

data_list = os.listdir(os.path.join(indir, 'data', year))
mc_list = os.listdir(os.path.join(indir, 'mc', year))

file_dict = {}
for data in data_list:
    data_path = os.path.join(indir, 'data', year, data)
    file_dict[data_path] = os.listdir(data_path)
for mc in mc_list:
    mc_path = os.path.join(indir, 'mc', year, mc)
    file_dict[mc_path] = os.listdir(mc_path)

syst_list = ["", "__jerup","__jerdown", "__jecAbsoluteup","__jecAbsolutedown",
             "__jecAbsolute_"+year[:4]+"up", "__jecAbsolute_"+year[:4]+"down",
             "__jecBBEC1up", "__jecBBEC1down", "__jecBBEC1_"+year[:4]+"up", "__jecBBEC1_"+year[:4]+"down",
             "__jecFlavorQCDup", "__jecFlavorQCDdown", "__jecRelativeBalup", "__jecRelativeBaldown",
             "__jecRelativeSample_"+year[:4]+"up", "__jecRelativeSample_"+year[:4]+"down"]
# tune and hdamp will appear as an individual dataset.
# thus no need to run in loop, but left here for double check
#syst1 = ["__tuneup", "__tunedown", "__hdampup", "__hdampdown",]

for path, flist in file_dict.items():
    for fname in flist:
        #test_list = []
        test_list = ["TTTo2L2Nu", "SingleMuon2018B"]
        #test_list = ["SingleMuon2018B"]
        #test_list = ['TTToSemiLeptonic']
        if len(test_list) > 0:
            if not any(i in path for i in test_list): continue
        if len(sys.argv) > 4:
            if dataOrMC == 'data':
                if 'data' not in path[5:]: continue
            elif dataOrMC == 'mc':
                if 'mc' not in path[5:]: continue

        syst = "all" #placeholder for mc all SF unc calculation

        for tmp_sys in syst_list:
            if "data" in path[5:]: #storage starts with /data1
                syst = "data"
                if tmp_sys != "": continue

            elif len(tmp_sys) > 0:
                syst = tmp_sys

            infile = os.path.join(path, fname)
            dataset = path.split('/')[-1] + tmp_sys 
            outputdir = os.path.join(tgdir, dataset)
            os.makedirs(os.path.join(outputdir), exist_ok=True)
            logdir = os.path.join(log, dataset)
            os.makedirs(logdir, exist_ok=True)


            runString = "sbatch scripts/job_slurm_process.sh " + year + " " + infile + " " + outputdir + " " + fname + " " + workdir + " " + logdir + " " + syst.replace('__','')

            print(runString)
            call([runString], shell=True)
