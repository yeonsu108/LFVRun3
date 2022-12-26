import os, sys
from subprocess import call

version = sys.argv[1] #folder under /data1/common/skimmed_NanoAOD/
output = sys.argv[2] #output folder in your working directory
year = sys.argv[3]
syst = sys.argv[4]
if len(sys.argv) > 5:
    dataOrMC = sys.argv[5] #'data' or 'mc'

workdir = os.getcwd()
indir = os.path.join('/data1/common/skimmed_NanoAOD/', version)
tgdir = os.path.join(workdir, output, year)
logdir = os.path.join(workdir, output, year, 'log')

os.makedirs(tgdir, exist_ok=True)
os.makedirs(logdir, exist_ok=True)

datadir = os.path.join(indir, 'data', year)
data_list = [os.path.join(datadir, s) for s in os.listdir(datadir)]
mcdir = os.path.join(indir, 'mc', year)
mc_list = [os.path.join(mcdir, s) for s in os.listdir(mcdir)]

dataset_list = data_list + mc_list

syst_list = ["", "__jerup","__jerdown", "__jesAbsoluteup","__jesAbsolutedown",
             "__jesAbsolute_"+year[:4]+"up", "__jesAbsolute_"+year[:4]+"down",
             "__jesBBEC1up", "__jesBBEC1down", "__jesBBEC1_"+year[:4]+"up", "__jesBBEC1_"+year[:4]+"down",
             "__jesFlavorQCDup", "__jesFlavorQCDdown", "__jesRelativeBalup", "__jesRelativeBaldown",
             "__jesRelativeSample_"+year[:4]+"up", "__jesRelativeSample_"+year[:4]+"down"]
# tune and hdamp will appear as an individual dataset.
# thus no need to run in loop, but left here for double check
syst_ext = ["__tuneup", "__tunedown", "__hdampup", "__hdampdown",]

# Default syst for MC = "theory" = all SF + theory
# To run central values only, pass "nosyst"
# To calculate theory uncertainties (PDF, ME, PS, if available), put 'theory'
# Data should use systematic flag "data" not to construct event weights

parameters = [] #order: (tgdir, indir, year, syst, json, False)
for ds in dataset_list:

    #if len(options.dataset) > 0 and not any(i in ds for i in options.dataset): continue

    for src in syst_list:

        if len(sys.argv) > 5 and dataOrMC == 'data':
            if 'data' not in ds[5:]: continue
        elif len(sys.argv) > 5 and dataOrMC == 'mc':
            if 'mc' not in ds[5:]: continue

        dataset_name = ds.split('/')[-1]
        outfname = os.path.join(tgdir, dataset_name + src + '.root')

        if 'data' in ds[5:]:
            if src == "":
                parameters.append([outfname, ds, year, "data"])
            else: continue

        else:
           if src == "":
              if syst == "all":
                  parameters.append((outfname, ds, year, "all", "", False))
              elif syst == "theory":
                  if any(i in dataset_name for i in ["TTTo", "TT_LFV", "ST_LFV"]): #include TTW,TTZ for theory unc?
                      parameters.append([outfname, ds, year, "theory"])
                  else: parameters.append([outfname, ds, year, "all"])
              elif syst == "nosyst":
                  parameters.append([outfname, ds, year, "nosyst"])
           else:
              #os.makedir(os.path.join(tgdir, dataset_name+src)
              if any(i in dataset_name for i in syst_ext): continue
              parameters.append([outfname, ds, year, src[2:]])


for item in parameters:
    runString = "sbatch scripts/job_slurm_process.sh " + item[2] + " " + item[1] + " " + item[0] + " " + logdir + " " + item[3]

    print(runString)
    #call([runString], shell=True)
