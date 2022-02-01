import os
import sys
os.environ["CUDA_VISIBLE_DEVICES"] = "3"
import uproot
import pandas as pd
import awkward as ak
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping, ModelCheckpoint
from utils.hists import *

base_dir = os.getcwd().replace("DNN","") # Upper directory
processed = "dec_02"
label = "jan01"
syst = "norm"
nodes = 20
layers = 3
sbratio = 1
systs = ["norm","jecup","jecdown","puup","pudown","btagup_jes","btagdown_jes"]
for syst in systs:
    for y in ["16pre","16post","17","18"]:
        for p in ["ST","TT"]:
            print("Start "+p+" LFV Evaluation")
            epochs = 1000
            nodes = 20
            layers = 3
            drop = -1.
            inputvars = []
            if p == "ST":
                inputvars = ["Sel_muon1pt","Sel_muon1eta","Sel_tau1pt","Sel_tau1eta",
                    "Sel2_jet1pt","Sel2_jet2pt","Sel2_jet3pt",
                    "Sel2_jet1eta","Sel2_jet2eta","Sel2_jet3eta",
                    "Sel2_jet1btag","Sel2_jet2btag","Sel2_jet3btag",
                    "Sys_METpt","Sys_METphi",
                    "chi2","chi2_SMW_mass","chi2_SMTop_mass"]
                sbratio = 1 # sig:bkg = 1:1
                nodes = 20
                layers = 2
            elif p == "TT":
                inputvars = ["Sel_muon1pt","Sel_muon1eta","Sel_tau1pt","Sel_tau1eta",
                    "Sel2_jet1pt","Sel2_jet2pt","Sel2_jet3pt","Sel2_jet4pt",
                    "Sel2_jet1eta","Sel2_jet2eta","Sel2_jet3eta","Sel2_jet4eta",
                    "Sel2_jet1btag","Sel2_jet2btag","Sel2_jet3btag","Sel2_jet4btag",
                    "Sys_METpt","Sys_METphi",
                    "chi2","chi2_lfvTop_mass","chi2_SMW_mass","chi2_SMTop_mass"]
                sbratio = 1 # sig:bkg = 1:1
                nodes = 15
                layers = 2

            project_dir = "nanoaodframe_"+p+"LFV/"+processed+"_"+syst+"/"+y+"/"    # MODIFY!!!
            path = base_dir+project_dir
            flist = os.listdir(path)
            flist = [i for i in flist if ".root" in i]
            
            train_dir = label+"/"+p+processed+"_norm_"+str(nodes)+"nodes_"+str(layers)+"layers_s1b"+str(sbratio)+"_"+label
            model_dir = train_dir+'/best_model.h5'
            model = tf.keras.models.load_model(model_dir)
            model.summary()
            
            eval_dir = label+"/"+p+processed+"_"+syst+"_"+str(nodes)+"nodes_"+str(layers)+"layers_s1b"+str(sbratio)+"_"+label

            weights = ["evWeight"]
            class_names = ["sig", "bkg"]
            hists_path = eval_dir+"/pred_hists/"+y+"/"
            if not os.path.isdir(hists_path):
                os.makedirs(hists_path)

            for f in flist:
                fdict = f.split("_"+y)[0]
                f_dir = path+f
                outf_dir = hists_path+f.replace(".root","")+"_pred.root"
                infile = uproot.open(f_dir)
                tree = infile["outputTree2"]
                hnocut = infile["hcounter_nocut"]
                hpglep = infile["hnevents_pglep_cut0000"]
                htot = infile["hnevents_cut0000"]
                if len(tree) == 0:
                    print("No events : "+f)
                    continue
                print(f)
                pd_data = tree.arrays(inputvars,library="pd")
                pd_weight = tree.arrays(weights,library="np")
                pred_data = np.array(pd_data.filter(items = inputvars))
                pred = model.predict(pred_data,batch_size=128)
                pred = pred[:,1]
                drawhist = hists(pd_data,pred,pd_weight)
                with uproot.recreate(outf_dir) as outf:
                    for key, hist in drawhist:
                        outf["h_"+key+"_pred"] = hist
                    outf["hcounter_nocut"] = hnocut
                    outf["hnevents_pglep_cut0000"] = hpglep
                    outf["hnevents_cut0000"] = htot
