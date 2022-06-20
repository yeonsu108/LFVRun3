import ROOT
from ROOT import *
import os
import sys
import tdrstyle
tdrstyle.setTDRStyle()
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)

base_dir = os.getcwd().replace("systematics/JEC","") # LFVRun2 repo. base dir
project = "mar_02"

hists_path = "./plots/"+project+"_ST"
if not os.path.isdir(hists_path):
    os.makedirs(hists_path)

rpath_norm = base_dir+"nanoaodframe_STLFV/plot_STLFV/"+project+"_norm/noblind/stackhist_137.65.root"
rpath_up = base_dir+"nanoaodframe_STLFV/plot_STLFV/"+project+"_jesup/noblind/stackhist_137.65.root"
rpath_down = base_dir+"nanoaodframe_STLFV/plot_STLFV/"+project+"_jesdown/noblind/stackhist_137.65.root"
print(rpath_norm)
f1 = TFile(rpath_norm)
f2 = TFile(rpath_up)
f3 = TFile(rpath_down)

hists = {
        #"hncleanjetspass":"Number of Jets",
        "hncleanbjetspass":"Number of b-tagged Jets",
        "hjet1pt"       :"p_{T} of Leading Jet (GeV)",
        "hjet2pt"       :"p_{T} of Sub-leading Jet (GeV)",
        "hjet3pt"       :"p_{T} of Third Jet (GeV)",
        "hjet1eta"      :"#eta of Leading Jet",
        "hjet2eta"      :"#eta of Sub-leading Jet",
        "hjet3eta"      :"#eta of Third Jet",
        "hjet1btag"     :"btag Discriminant of Leading Jet",
        "hjet2btag"     :"btag Discriminant of Sub-leading Jet",
        "hjet3btag"     :"btag Discriminant of Third Jet",
        "hbjet1pt"      :"p_{T} of b-tagged Jet (GeV)",
        "hbjet1eta"     :"#eta of b-tagged Jet",
        "hmuon1pt"      :"p_{T} of Muon (GeV)",
        "hmuon1eta"     :"#eta of Muon",
        "hmuMETmt"      :"m_{T} (GeV)",
        "htau1pt"       :"p_{T} of Hadronic Tau (GeV)",
        "htau1eta"      :"#eta of Hadronic Tau",
        #"htau1mass"     :"Mass of Hadronic Tau (GeV)",
        "hmutau_dEta"   :"d#eta_{#mu#tau}",
        "hmutau_dPhi"   :"d#phi_{#mu#tau}",
        "hmutau_dR"     :"dR_{#mu#tau}",
        "hmutau_mass"   :"m_{#mu#tau} (GeV)",
        "hmetpt"        :"MET (GeV)",
        "hmetphi"       :"#phi_{MET}",
        "hchi2"         :"#chi^{2}",
        "hchi2_SMTop_mass"      :"SM Top mass (GeV)",
        "hchi2_SMW_mass"        :"SM W mass (GeV)",
        "hchi2_wqq_dEta"        :"#it{#Delta#eta}_{wqq}",
        "hchi2_wqq_dPhi"        :"#it{#Delta#phi}_{wqq}",
        "hchi2_wqq_dR"          :"#DeltaR_{wqq}"}

mcdata = ["mc"]
for d in mcdata:
    for key, value in hists.items():
        hname = "hstacked_"+d+"_"+key+"_cut00000"
        print(hname)
        h1 = f1.Get(hname)
        h2 = f2.Get(hname)
        h3 = f3.Get(hname)

        h2.Divide(h1)
        h3.Divide(h1)
        h1.Divide(h1)
        h1.SetLineStyle(1)
        h2.SetLineStyle(3)
        h3.SetLineStyle(7)
        h1.SetLineColor(1)
        h2.SetLineColor(1)
        h3.SetLineColor(1)
        h1.SetLineWidth(2)
        h2.SetLineWidth(2)
        h3.SetLineWidth(2)

        hmax = max([h1.GetMaximum(),h2.GetMaximum(),h3.GetMaximum()])

        h1.GetXaxis().SetTitle(value)
        c1 = TCanvas('c','c',600,600)
        c1.cd()
        c1.SetMargin(0.1,0.05,0.1,0.05)
        h1.Draw("hist")
        h2.Draw("histsame")
        h3.Draw("histsame")
        
        leg = TLegend(0.45,0.7,0.8,0.93)
        gStyle.SetLegendTextSize(0.04)
        leg.SetBorderSize(0)
        leg.AddEntry(h1,"Nominal")
        leg.AddEntry(h2,"JESup")
        leg.AddEntry(h3,"JESdown")
        leg.Draw()
        
        c1.Print(hists_path+"/hJES_"+d+"_"+key+".pdf")
        c1.Close()

for d in mcdata:
    for key, value in hists.items():
        hname = "hstacked_"+d+"_"+key+"_cut00000"
        h1 = f1.Get(hname)
        h2 = f2.Get(hname)
        h3 = f3.Get(hname)

        h2.Divide(h1)
        h3.Divide(h1)
        h1.Divide(h1)
        h1.SetLineStyle(1)
        h2.SetLineStyle(3)
        h3.SetLineStyle(7)
        h1.SetLineColor(1)
        h2.SetLineColor(1)
        h3.SetLineColor(1)
        h1.SetLineWidth(2)
        h2.SetLineWidth(2)
        h3.SetLineWidth(2)

        hmax = max([h1.GetMaximum(),h2.GetMaximum(),h3.GetMaximum()])
        hmin = min([h1.GetMinimum(),h2.GetMinimum(),h3.GetMinimum()])
        hmin = hmax if hmin == 0 else hmin
        hrange = max(hmax-1,1-hmin)
        h1.SetMaximum((1+hrange)*1.2)
        h1.SetMinimum((1-hrange)/1.2)

        h1.GetXaxis().SetTitle(value)
        c1 = TCanvas('c','c',600,600)
        c1.cd()
        c1.SetMargin(0.1,0.05,0.1,0.05)
        h1.Draw("hist")
        h2.Draw("histsame")
        h3.Draw("histsame")
        
        leg = TLegend(0.45,0.7,0.8,0.93)
        gStyle.SetLegendTextSize(0.04)
        leg.SetBorderSize(0)
        leg.AddEntry(h1,"Nominal")
        leg.AddEntry(h2,"JESup")
        leg.AddEntry(h3,"JESdown")
        leg.Draw()
        
        c1.Print(hists_path+"/hJES_"+d+"_"+key+".pdf")
        c1.Close()
f1.Close()
f2.Close()
f3.Close()
