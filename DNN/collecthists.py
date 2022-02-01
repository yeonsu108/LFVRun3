import ROOT
import os
import sys

projname = "dec_02"
dnnname = "30nodes_2layers_s1b1"
label = "jan01"
lfvprocs = ["ST","TT"]
hists = ["data_obs","hstacked_mc_h_dnn_pred",
        "LFV_STc_s","LFV_STc_v","LFV_STc_t","LFV_STu_s","LFV_STu_v","LFV_STu_t",
        "LFV_TTc_s","LFV_TTc_v","LFV_TTc_t","LFV_TTu_s","LFV_TTu_v","LFV_TTu_t",
        "TT","ST","DY","Wjets","Oth"]

systs = {"norm":"norm","jecup":"jecUp","jecdown":"jecDown","puup":"puUp","pudown":"puDown","btagup_jes":"btag_jesUp","btagdown_jes":"btag_jesDown"}
runs = ["run16APV","run16","run17","run18","run2"]
outfolder = "./pred_"+label
if not os.path.isdir(outfolder):
    os.makedirs(outfolder)
for run in runs:
    rname = ""
    if run == "run16APV":
        rname = "stackhist_19.5.root"
    elif run == "run16":
        rname = "stackhist_16.8.root"
    elif run == "run17":
        rname = "stackhist_41.48.root"
    elif run == "run18":
        rname = "stackhist_59.83.root"
    elif run == "run2":
        rname = "stackhist_137.65.root"
    for lfvproc in lfvprocs:
        outfname = ""
        if lfvproc == "ST":
            dnnname = "20nodes_2layers_s1b1"
            outfname = "pred_"+label+"/pred_"+run+"_cat1.root"
        elif lfvproc == "TT":
            dnnname = "15nodes_2layers_s1b1"
            outfname = "pred_"+label+"/pred_"+run+"_cat2.root"
        outf = ROOT.TFile(outfname,"RECREATE")
        for key, value in systs.items():
            infilename = label + "/"+lfvproc+projname+"_"+key+"_"+dnnname+"_"+label+"/pred_hists/"+rname
            inf = ROOT.TFile(infilename)
            outf.cd()
            for h in hists:
                tmphist = inf.Get(h)
                if not tmphist:
                    print("wrong hist",h)
                    continue
                copyhname = h
                if key is not "norm":
                    copyhname = h+"_"+value
                print(copyhname)
                tmphist_copy = tmphist.Clone(copyhname)
                tmphist_copy.Write()
            inf.Close()
        outf.Close()
