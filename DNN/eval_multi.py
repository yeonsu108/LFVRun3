import os
import sys
os.environ["CUDA_VISIBLE_DEVICES"] = "3"
import uproot
import pandas as pd
import awkward as ak
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow.keras.backend as K
from keras.callbacks import EarlyStopping, ModelCheckpoint
import multiprocessing

base_dir = os.getcwd().replace("DNN","") # Upper directory
processed = "aug22"
label = "rerun_merged_3"
systs = ['nom','puup', 'pudown', 'btagup_hf', 'btagdown_hf', 'btagup_lf', 'btagdown_lf', 'btagup_hfstats1', 'btagdown_hfstats1', 'btagup_hfstats2', 'btagdown_hfstats2', 'btagup_lfstats1', 'btagdown_lfstats1', 'btagup_lfstats2', 'btagdown_lfstats2', 'btagup_cferr1', 'btagdown_cferr1', 'btagup_cferr2', 'btagdown_cferr2', 'up_jesAbsolute', 'down_jesAbsolute', 'up_jesBBEC1', 'down_jesBBEC1', 'up_jesEC2', 'down_jesEC2', 'up_jesFlavorQCD', 'down_jesFlavorQCD', 'up_jesRelativeBal', 'down_jesRelativeBal', 'up_jesAbsolute_year', 'down_jesAbsolute_year', 'up_jesBBEC1_year', 'down_jesBBEC1_year', 'up_jesEC2_year', 'down_jesEC2_year', 'up_jesRelativeSample_year', 'down_jesRelativeSample_year']

inputvars = ["Sel_muon1pt","Sel_muon1eta",
"Sel_tau1pt","Sel_tau1eta","Sel_tau1mass",
"Sel2_jet1pt","Sel2_jet2pt","Sel2_jet3pt",
"Sel2_jet1eta","Sel2_jet2eta","Sel2_jet3eta",
"Sel2_jet1mass","Sel2_jet2mass","Sel2_jet3mass",
"Sel2_jet1btag","Sel2_jet2btag","Sel2_jet3btag",
"Sys_METpt","Sys_METphi",
"chi2","chi2_SMW_mass","chi2_SMTop_mass",
"chi2_wqq_dEta","chi2_wqq_dPhi","chi2_wqq_dR",
"mutau_mass","mutau_dEta","mutau_dPhi","mutau_dR",
]
#infile_dict = {"st":("hnevents_cut00000",2),"tt":("hnevents_cut000000",1), "bkg":("",0)}
#infile_dict = {"st":("hnevents_cut00000",2),"tt":("hnevents_cut00000",1), "bkg":("hnevents_cut00000",0)}
infile_dict = {"dummy":("hnevents_cut00000",2)}#,"tt":("hnevents_cut00000",1), "bkg":("hnevents_cut00000",0)}
discriminators = {"p_st" : 2, "p_tt" : 1 , "p_bkg" : 0 , "p_st_tt" : 999, "p_st_tt_ob" : 999 }

def run(inputs):
    year = inputs[0]
    syst = inputs[1]
    #ch   = inputs[2]
    discriminator_key = inputs[2]
    alpha = inputs[3]

    if 'year' in syst:
        syst_ = syst.replace('year', year)
    else: syst_ = syst

    binedges = [0,0.1,0.3,0.7,0.9,1.0]
    if "ob" in discriminator_key : binedges = np.linspace(0.0, 200.0, num=21).tolist()

    p="Multi"
    print("Start "+p+" LFV Evaluation")
    #if ch=="bkg" :
    #project_dir = "/data1/users/ecasilar/processed_LFV/aug22_mergedlfv/"+syst+"/"+year+"/"
    #project_dir = "/data1/users/itseyes/LFV/processed_LFV/merged//"+syst+"/"+year+"/"
    project_dir = "/data1/users/itseyes/LFV/processed_LFV/nov16//"+syst+"/"+year+"/"
    path = project_dir
    flist = os.listdir(path)
    flist = [i for i in flist if ".root" in i]
    #else:
    #project_dir = "/home/itseyes/github/LFVRun2_ndf_integration/nanoaodframe/aug22_"+ch+"lfv/"+syst+"/"+year+"/"
    #project_dir = "/data1/users/itseyes/LFV/processed_LFV/merged/"+syst+"/"+year+"/"
    #path = project_dir
    #flist = os.listdir(path)
    #flist = [i for i in flist if ("LFV" in i) and (".root" in i)]
    print(flist)
    
    model_dir = label+"_"+p+processed+"/nom/best_model.h5"
    #print(model_dir)
    model = tf.keras.models.load_model(model_dir)
    #model.summary()
    
    eval_dir = label+"_"+p+processed+"/"
    
    weights = ["evWeight"]
    hists_path = eval_dir+"/"+year+"/preds/"+discriminator_key+"/"+str(alpha).replace(".","p")+"/"
    if not os.path.isdir(hists_path):
        os.makedirs(hists_path)
    
    for f in flist:
        syst__ = ""
        if syst == "nom": syst__ = ""
        else: syst__ = "__" + syst_
        #outf_dir = hists_path+f.replace("_"+year+"_"+syst+".root","_"+ch+"_pred"+syst__+".root")
        #if ch == "bkg" : outf_dir = hists_path+f.replace("_"+year+"_"+syst+".root",syst__+".root")
        outf_dir = hists_path+f.replace("_"+year+"_"+syst+".root",syst__+".root")
        #else : outf_dir = hists_path+f.replace("_"+year+"_"+syst+".root","_"+ch+syst__+".root")
        f_dir = path+f
        infile = uproot.open(f_dir)
        tree = infile["outputTree2"]
        hnocut = infile["hcounter_nocut"]
        hpglepweight = infile["hnevents_pglep_cut0000"]
        hfullweight = infile["hnevents_cut0000"]
        #if ch=="bkg":
        #        hfinal_st = infile[infile_dict["st"][0]]
        #        hfinal_tt = infile[infile_dict["tt"][0]]
        #else:
        hfinal = infile[infile_dict["dummy"][0]]
	
        if len(tree) == 0:
            print("No events : "+f)
            pred = []
            pd_weight = []
            dnnhist = np.histogram(pred,bins=binedges,weights=pd_weight,density=False)
            dnnhist_entries = np.histogram(pred,bins=binedges,density=False)
        else:
            print("Good file :",f)
            pd_data = tree.arrays(inputvars,library="pd")
            pd_weight = tree.arrays(weights,library="np")
            pred_data = np.array(pd_data.filter(items = inputvars))
            pred = model.predict(pred_data,batch_size=128, workers=1, use_multiprocessing=False)
            if discriminator_key == "p_st_tt_ob"  : 
                 rmzeros = pred[:,0] 
                 rmzeros[rmzeros<=0.00] = 0.001
                 pred[:,0] = rmzeros
                 pred = (((1-alpha)*pred[:,2]+alpha*pred[:,1])/pred[:,0]).tolist()
                 pred = np.array(pred)
                 pred[pred>=190] = 190
                 pred = pred.tolist()
            elif discriminator_key == "p_st_tt"  : pred = (pred[:,2]+pred[:,1]).tolist()
            elif discriminator_key == "p_max"  : pred = (np.amax(pred, axis=1)).tolist()
            elif discriminator_key == "p_mean"  : pred = (np.mean(pred, axis=1)).tolist()
            elif discriminator_key == "p_min"  : pred = (np.min(pred, axis=1)).tolist()
            else  : pred = (pred[:,discriminators[discriminator_key]]).tolist()
            pd_weight = pd_weight['evWeight'].tolist()
            dnnhist = np.histogram(pred,bins=binedges,weights=pd_weight,density=False)
            dnnhist_entries = np.histogram(pred,bins=binedges,density=False)
        with uproot.recreate(outf_dir) as outf:
            outf["h_dnn_pred"] = dnnhist
            outf["h_dnn_entries"] = dnnhist_entries
            outf["hcounter_nocut"] = hnocut
            outf["hnevents_pglep_cut0000"] = hpglepweight
            outf["hnevents_cut0000"] = hfullweight
            #if ch=="bkg": 
            #outf["hnevents_final_st"] = hfinal_st
            ##outf["hnevents_final_tt"] = hfinal_tt
            #else:
            outf["hnevents_final"] = hfinal

    K.clear_session()

if __name__ == '__main__':

    parameters = []
    #for discriminator in ["p_st","p_tt","p_bkg","p_st_tt","p_st_tt_ob"]:
    for discriminator in ["p_st_tt_ob"]:
      #for alpha in np.around(np.linspace(0.1, 0.9, num=9),decimals=1).tolist():
      for alpha in [0.1]:
         #for year in ["16pre","16post","17","18"]:
         for year in ["16pre"]:
            for syst in systs:
               parameters.append((year, syst, discriminator,alpha))

    pool = multiprocessing.get_context("spawn").Pool(10)
    pool.map(run, parameters)
    pool.close()
    pool.join()
