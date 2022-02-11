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
nodes = 20
layers = 3
sbratio = 1
systs = ["norm",
        "jecup","jecdown",
        "puup","pudown",
        "btagup_jes","btagdown_jes",
        "btagup_hf","btagdown_hf",
        "btagup_lf","btagdown_lf",
        ]
for syst in systs:
    for y in ["16pre","16post","17","18"]:
        for p in ["ST","TT"]:
            print("Start "+p+" LFV Evaluation")
            epochs = 1000
            nodes = 20
            layers = 3
            inputvars = []
            if p == "ST":
                inputvars = ["Sel_muon1pt","Sel_muon1eta","Sel_muon1mass",
                    "Sel_tau1pt","Sel_tau1eta","Sel_tau1mass",
                    "Sel2_jet1pt","Sel2_jet2pt","Sel2_jet3pt",
                    "Sel2_jet1eta","Sel2_jet2eta","Sel2_jet3eta",
                    "Sel2_jet1mass","Sel2_jet2mass","Sel2_jet3mass",
                    "Sel2_jet1btag","Sel2_jet2btag","Sel2_jet3btag",
                    "Sys_METpt","Sys_METphi",
                    "chi2","chi2_SMW_mass","chi2_SMTop_mass",
                    ]
                sbratio = 1 # sig:bkg = 1:1
                nodes = 20
                layers = 2
            elif p == "TT":
                inputvars = ["Sel_muon1pt","Sel_muon1eta","Sel_muon1mass",
                    "Sel_tau1pt","Sel_tau1eta","Sel_tau1mass",
                    "Sel2_jet1pt","Sel2_jet2pt","Sel2_jet3pt","Sel2_jet4pt",
                    "Sel2_jet1eta","Sel2_jet2eta","Sel2_jet3eta","Sel2_jet4eta",
                    "Sel2_jet1mass","Sel2_jet2mass","Sel2_jet3mass","Sel2_jet4mass",
                    "Sel2_jet1btag","Sel2_jet2btag","Sel2_jet3btag","Sel2_jet4btag",
                    "Sys_METpt","Sys_METphi",
                    "chi2","chi2_lfvTop_mass","chi2_SMW_mass","chi2_SMTop_mass",
                    "chi2_wqq_dEta","chi2_wqq_dPhi","chi2_wqq_dR",
                    "chi2_lfvjmu_dEta","chi2_lfvjmu_dPhi","chi2_lfvjmu_dR","chi2_lfvjmu_mass",
                    "chi2_lfvjtau_dEta","chi2_lfvjtau_dPhi","chi2_lfvjtau_dR","chi2_lfvjtau_mass",
                    "chi2_lfvjmutau_dEta","chi2_lfvjmutau_dPhi","chi2_lfvjmutau_dR","chi2_lfvjmutau_mass"
                    ]
                sbratio = 1 # sig:bkg = 1:1
                nodes = 15
                layers = 2

            project_dir = "nanoaodframe_"+p+"LFV/"+processed+"_"+syst+"/"+y+"/"    # MODIFY!!!
            path = base_dir+project_dir
            flist = os.listdir(path)
            flist = [i for i in flist if ".root" in i]
            
            train_dir = label+"_"+p+processed+"_"+str(nodes)+"nodes_"+str(layers)+"layers_s1b"+str(sbratio)+"/norm"
            model_dir = train_dir+'/best_model.h5'
            model = tf.keras.models.load_model(model_dir)
            model.summary()
            
            eval_dir = label+"_"+p+processed+"_"+str(nodes)+"nodes_"+str(layers)+"layers_s1b"+str(sbratio)+"/"+syst

            weights = ["evWeight"]
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
                dnnhist = np.histogram(pred,20,(0.0,1.0),pd_weight,density=False)
                with uproot.recreate(outf_dir) as outf:
                    outf["h_dnn_pred"] = dnnhist
                    outf["hcounter_nocut"] = hnocut
                    outf["hnevents_pglep_cut0000"] = hpglep
                    outf["hnevents_cut0000"] = htot
