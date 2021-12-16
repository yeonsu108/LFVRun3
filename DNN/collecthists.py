import ROOT
import os
import sys

projname = "dec_02"
dnnname = "30nodes_2layers_s1b1"
lfvprocs = ["ST","TT"]
hists = ["data_obs","hstacked_mc_h_dnn_pred",
        "LFV_STc_s","LFV_STc_v","LFV_STc_t","LFV_STu_s","LFV_STu_v","LFV_STu_t",
        "LFV_TTc_s","LFV_TTc_v","LFV_TTc_t","LFV_TTu_s","LFV_TTu_v","LFV_TTu_t",
        "TT","ST","DY","Wjets","Oth"]

systs = {"norm":"norm","jecup":"jecUp","jecdown":"jecDown"}
for lfvproc in lfvprocs:
    outfname = "pred_"+lfvproc+"LFV_"+projname+".root"
    outf = ROOT.TFile(outfname,"RECREATE")
    for key, value in systs.items():
        infilename = lfvproc+projname+"_"+key+"_"+dnnname+"/pred_hists/stackhist_137.65.root"
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
