import ROOT
import os
import sys
basepath = "TopLFV/GenAnalyzer/oldrootfiles/"

rfilenames = ["LFV_TT_to_cmutau_Ceu_2018_GenAna_v1.root",
        "LFV_TT_to_cmutau_Clq_2018_GenAna_v1.root",
        "LFV_TT_to_cmutau_Clu_2018_GenAna_v1.root",
        "LFV_TT_to_cmutau_Cqe_2018_GenAna_v1.root",
        "LFV_TT_to_cmutau_Clequ1_2018_GenAna_v1.root",
        "LFV_TT_to_cmutau_Clequ3_2018_GenAna_v1.root",]

initialHistnames = ["bSMpt","bSMeta","cLFVpt","cLFVeta",
        "muLFVpt","muLFVeta","tauLFVpt","tauLFVeta",
        "lepLFVdR","lepLFVmass"]

finalHistnames = ["h_bpt","h_beta","h_cpt","h_ceta",
        "h_mupt","h_mueta","h_taupt","h_taueta",
        "h_lepdR","h_lepmass"]

for r in rfilenames:
    inf = ROOT.TFile(basepath + r)
    print(inf)
    outfname = ""
    if "Ceu" in r:
        outfname = "LFV_TT_to_cmutau_Ceu.root"
    elif "Clq" in r:
        outfname = "LFV_TT_to_cmutau_Clq.root"
    elif "Clu" in r:
        outfname = "LFV_TT_to_cmutau_Clu.root"
    elif "Cqe" in r:
        outfname = "LFV_TT_to_cmutau_Cqe.root"
    elif "Clequ1" in r:
        outfname = "LFV_TT_to_cmutau_Clequ1.root"
    elif "Clequ3" in r:
        outfname = "LFV_TT_to_cmutau_Clequ3.root"
    outf = ROOT.TFile("rootfiles/"+outfname,"RECREATE")
    outf.cd()
    for i, ahist in enumerate(initialHistnames):
        tmphist = inf.Get("genana/"+ahist)
        if tmphist:
            print("hist exists")
            tmphist_copy = tmphist.Clone(finalHistnames[i])
            tmphist_copy.Write()
    outf.Close()
    inf.Close()
