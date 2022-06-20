import os
import sys
import uproot
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt

base_dir = os.getcwd() # Upper directory
processed = "dec_02"
label = "jan01"
systs = ["norm",
        "jecup","jecdown",
        "puup","pudown",
        "btagup_jes","btagdown_jes",
        "btagup_hf","btagdown_hf",
        "btagup_lf","btagdown_lf",
        ]
hists_path = "./test_plots/"
if not os.path.isdir(hists_path):
    os.makedirs(hists_path)
outf_dir = hists_path+"TTTo2L2Nu_test_plots.root" 
with uproot.recreate(outf_dir) as outf:
    for syst in systs: 
        project_dir = "/nanoaodframe_STLFV/"+processed+"_"+syst+"/"
        path = base_dir+project_dir
        
        weights = ["evWeight"]

        f_dir = path+"TTTo2L2Nu_norm.root"
        infile = uproot.open(f_dir)
        tree = infile["outputTree2"]
        if len(tree) == 0:
            print("No events : "+f)
            continue
        pd_weight = tree.arrays(weights,library="np")
        print(pd_weight)
        hist = np.histogram(pd_weight["evWeight"],40,(0.0,4.0))
        outf["hevWeights_"+syst] = hist
