import os
import sys
import ROOT
from ROOT import *
import numpy as np

base_path = './'
if len(sys.argv) > 1:
    base_path += sys.argv[1]
if not os.path.exists(base_path):
    print("Folder '{}' does not exists.".format(base_path))
else:
    print("Start postprocessing at '{}'.".format(base_path))

# Set Runs
runs = ['16pre', '16post', '17', '18']

# Set output folders
out_path = base_path+'/postprocess'
if not os.path.exists(out_path):
    for run in runs:
        os.makedirs(out_path + '/' + run)


# Produce dictionary for file lists.
file_list = {}
for run in runs:
    file_list[run] = [i for i in os.listdir(base_path+'/'+run) if ".root" in i]

def get_bSFratio(infile):
    prehist = infile.Get('hnevents_pglep_cut000')
    posthist = infile.Get('hnevents_cut000')
    if prehist.Integral() * posthist.Integral() == 0:
        return 1
    return posthist.Integral() / prehist.Integral()

# Loop over all files.
for run in runs:
    for fname in file_list[run]:
        #print(os.path.join(base_path,run,fname))
        infile = TFile.Open(os.path.join(base_path,run,fname), 'READ')
        hlists = [ h.GetName() for h in infile.GetListOfKeys() if 'cut' in h.GetName() ]
        ratio = get_bSFratio(infile)
        outfile = TFile.Open(os.path.join(out_path,run,fname), 'RECREATE')
        for h in hlists:
            if ('event' in h) or ('counter' in h):
                continue
            if h[:2] == 'h1':
                continue
            if 'cut0000' in h:
                infile.cd()
                newhist = infile.Get(h)
                newhist.Scale(ratio)
                outfile.cd()
                newhist.Write()
        infile.Close()
        outfile.Close()
