import sys
import os
import ROOT
from ROOT import *
import tdrstyle
tdrstyle.setTDRStyle()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetLegendTextSize(0.04)

basepath = "/home/ljw1015/LFVRun2/DNN/pred_jan01/"
runs = ["run16APV","run16","run17","run18","run2"]
cats = ["cat1","cat2"]
systs = ["jec","pu","btag_jes","btag_hf","btag_lf"]
colors = [ROOT.TColor.GetColor(2),
        ROOT.TColor.GetColor(4),
        ROOT.TColor.GetColor(6),
        ROOT.TColor.GetColor(7),
        ROOT.TColor.GetColor(8),
        ]
colors = [2,4,6,7,8]
systcolor = dict(zip(systs,colors))
outdir = "./plot"
if not os.path.isdir(outdir):
    os.makedirs(outdir)

for run in runs:
    for cat in cats:
        print(run, cat)
        rfilename = "pred_"+run+"_"+cat+".root"
        f = TFile(basepath+rfilename)
        hnormname = "hstacked_mc_h_dnn_pred"
        hnorm = f.Get(hnormname)
        print(hnorm)
        hups = {}
        hdowns = {}
        hmaxs = []
        hmins = []

        # Obtaining Histograms from files.
        for syst in systs:
            hname = "hstacked_mc_h_dnn_pred_"+syst
            h1 = f.Get(hname+"Up")
            h2 = f.Get(hname+"Down")
            h1.Divide(hnorm)
            h2.Divide(hnorm)
            hups[syst] = h1
            hdowns[syst] = h2
            hmaxs.append(h1.GetMaximum())
            hmaxs.append(h2.GetMaximum())
            hmins.append(h1.GetMinimum())
            hmins.append(h2.GetMinimum())

        hmax = max(hmaxs)
        hmin = min(hmins)
        hmin = hmax if hmin == 0 else hmin
        hrange = max(hmax-1,1-hmin)
        
        # Drawing on Canvas with Legends
        c1 = TCanvas('c','c',600,600)
        c1.cd()
        c1.SetMargin(0.1,0.05,0.1,0.05)
        leg = TLegend(0.45,0.7,0.8,0.93)
        leg.SetBorderSize(0)
        
        for syst in systs:
            h1 = hups[syst]
            h2 = hdowns[syst]
            h1.SetLineWidth(2)
            h2.SetLineWidth(2)
            h1.SetLineColor(systcolor[syst])
            h2.SetLineColor(systcolor[syst])
            h1.GetXaxis().SetTitle("DNN output")
            h1.SetMaximum((1+hrange)*1.2)
            h1.SetMinimum((1-hrange)/1.2)
            h1.Draw("histsame")
            h2.Draw("histsame")
            leg.AddEntry(h1,syst, 'F')
        
        leg.Draw()
        c1.Print(outdir+"/Syst_DNNoutput_"+run+"_"+cat+".pdf")
        c1.Close()
        f.Close()
