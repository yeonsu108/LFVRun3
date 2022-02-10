import sys
import argparse
from utils import *

tdrstyle.setTDRStyle()
# Subplot ( Ratio plot : option -R, --ratio (default) / significance plot :  option -S, --significance )
parser = argparse.ArgumentParser()
parser.add_argument('-R', '--ratio', dest='ratio', action='store_true', default=False)
parser.add_argument('-S', '--significance', dest='significance', action='store_true', default=False)
parser.add_argument('-L', '--logstyle', dest='logstyle', action='store_true', default=False)
parser.add_argument('-Y', '--year', dest='year', type=str, default="")
parser.add_argument('-B', '--blind', dest='isblind', action='store_true', default=False)
args = parser.parse_args()
logstyle = args.logstyle
ratio = args.ratio
significance = args.significance
year = args.year
isblind = args.isblind

CMS_lumi.lumi_13TeV = "59.8 fb^{-1}"
s = stackhists.Stackhists(59.83)
year=str(year)
s.setupStyle(alpha=1)
CMS_lumi.extraText = ""
#CMS_lumi.extraText = "Simulation"

# DATA
s.addChannel("data18.root", "data", 999, isMC=False)

# MC ( reference twiki : https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns )

# W+Jets
s.addChannel("WJetsToLNu_HT-0To100.root", "W+jets", 3, isMC=True, xsec=61526700*0.9647, counterhistogramroot="WJetsToLNu_HT-0To100.root")
s.addChannel("WJetsToLNu_HT-100To200.root", "W+jets", 3, isMC=True, xsec=1345000.0*0.993, counterhistogramroot="WJetsToLNu_HT-100To200.root")
s.addChannel("WJetsToLNu_HT-200To400.root", "W+jets", 3, isMC=True, xsec=359700.0*1.002, counterhistogramroot="WJetsToLNu_HT-200To400.root")
s.addChannel("WJetsToLNu_HT-400To600.root", "W+jets", 3, isMC=True, xsec=48910.0*1.009, counterhistogramroot="WJetsToLNu_HT-400To600.root")
s.addChannel("WJetsToLNu_HT-600To800.root", "W+jets", 3, isMC=True, xsec=12050.0*1.120, counterhistogramroot="WJetsToLNu_HT-600To800.root")
s.addChannel("WJetsToLNu_HT-800To1200.root", "W+jets", 3, isMC=True, xsec=5501.0*1.202, counterhistogramroot="WJetsToLNu_HT-800To1200.root")
s.addChannel("WJetsToLNu_HT-1200To2500.root", "W+jets", 3, isMC=True, xsec=1329.0*1.332, counterhistogramroot="WJetsToLNu_HT-1200To2500.root")
s.addChannel("WJetsToLNu_HT-2500ToInf.root", "W+jets", 3, isMC=True, xsec=32.16*4.200, counterhistogramroot="WJetsToLNu_HT-2500ToInf.root")

# QCD
s.addChannel("QCD_Pt-15To20_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=1273190000000*0.003, counterhistogramroot="QCD_Pt-15To20_MuEnrichedPt5.root")
s.addChannel("QCD_Pt-20To30_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=558528000000*0.0053, counterhistogramroot="QCD_Pt-20To30_MuEnrichedPt5.root")
s.addChannel("QCD_Pt-30To50_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=139803000000*0.01182, counterhistogramroot="QCD_Pt-30To50_MuEnrichedPt5.root")
s.addChannel("QCD_Pt-50To80_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=19222500000*0.02276, counterhistogramroot="QCD_Pt-50To80_MuEnrichedPt5.root")
s.addChannel("QCD_Pt-80To120_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=2758420000*0.03844, counterhistogramroot="QCD_Pt-80To120_MuEnrichedPt5.root")
s.addChannel("QCD_Pt-120To170_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=469797000*0.05362, counterhistogramroot="QCD_Pt-120To170_MuEnrichedPt5.root")
s.addChannel("QCD_Pt-170To300_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=117989000*0.07335, counterhistogramroot="QCD_Pt-170To300_MuEnrichedPt5.root")
s.addChannel("QCD_Pt-300To470_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=7820250*0.10196, counterhistogramroot="QCD_Pt-300To470_MuEnrichedPt5.root")
s.addChannel("QCD_Pt-470To600_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=645528*0.12242, counterhistogramroot="QCD_Pt-470To600_MuEnrichedPt5.root")
s.addChannel("QCD_Pt-600To800_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=187109*0.13412, counterhistogramroot="QCD_Pt-600To800_MuEnrichedPt5.root")
s.addChannel("QCD_Pt-800To1000_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=32348.6*0.14552, counterhistogramroot="QCD_Pt-800To1000_MuEnrichedPt5.root")

# DY
s.addChannel("DYJetsToLL_M-10to50.root", "Z+jets", 4, isMC=True, xsec=18610000.0, counterhistogramroot="DYJetsToLL_M-10to50.root")
s.addChannel("DYJetsToLL_M-50_amcatnlo.root", "Z+jets", 4, isMC=True, xsec=6077220.0, counterhistogramroot="DYJetsToLL_M-50_amcatnlo.root")
#s.addChannel("DYJetsToLL_M-50_madgraph.root", "Z+jets", 4, isMC=True, xsec=6077220.0, counterhistogramroot="DYJetsToLL_M-50_madgraph.root")

s.addChannel("QCD_Pt-1000_MuEnrichedPt5.root", "QCD", 8, isMC=True, xsec=10430.5*0.15544, counterhistogramroot="QCD_Pt-1000_MuEnrichedPt5.root")

# ST
s.addChannel("ST_t-channel_top.root", "ST", 5, isMC=True, xsec=136020.0, counterhistogramroot="ST_t-channel_top.root")
s.addChannel("ST_t-channel_antitop.root", "ST", 5, isMC=True, xsec=80950.0, counterhistogramroot="ST_t-channel_antitop.root")
s.addChannel("ST_tW_top.root", "ST", 5, isMC=True, xsec=35850.0, counterhistogramroot="ST_tW_top.root")
s.addChannel("ST_tW_antitop.root", "ST", 5, isMC=True, xsec=35850.0, counterhistogramroot="ST_tW_antitop.root")

# TTbar
s.addChannel("TTTo2L2Nu.root", "TT-di", 0, isMC=True, xsec=88290.0, counterhistogramroot="TTTo2L2Nu.root")
s.addChannel("TTToSemiLeptonic.root", "TT-semi", 1, isMC=True, xsec=365340.0, counterhistogramroot="TTToSemiLeptonic.root")

# Other
s.addChannel("TTWJetsToLNu.root", "Other", 6, isMC=True, xsec=204.3, counterhistogramroot="TTWJetsToLNu.root")
s.addChannel("TTWJetsToQQ.root", "Other", 6, isMC=True, xsec=406.2, counterhistogramroot="TTWJetsToQQ.root")
s.addChannel("TTZToLLNuNu.root", "Other", 6, isMC=True, xsec=252.9, counterhistogramroot="TTZToLLNuNu.root")
s.addChannel("TTZToQQ.root", "Other", 6, isMC=True, xsec=529.7, counterhistogramroot="TTZToQQ.root")
s.addChannel("TTToHadronic.root", "Other", 6, isMC=True, xsec=377960.0, counterhistogramroot="TTToHadronic.root")
s.addChannel("WW.root", "Other", 6, isMC=True, xsec=118700.0, counterhistogramroot="WW.root")
s.addChannel("WZ.root", "Other", 6, isMC=True, xsec=47130.0, counterhistogramroot="WZ.root")
s.addChannel("ZZ.root", "Other", 6, isMC=True, xsec=16523.0, counterhistogramroot="ZZ.root")


# Histograms
# Muon Histograms
s.addHistogram("hmuon1pt", "p_{T} of Muon (GeV)", "Entries", drawmode=stackhists.STACKED, drawoption="hist", isLogy=logstyle, ymin=0.1)
s.addHistogram("hmuon1eta", "#eta of Muon", "Entries", drawmode=stackhists.STACKED, drawoption="hist", isLogy=logstyle, ymin=0.1)

# Sub-plot option
subplot="R"
if ratio : subplot="R"
elif significance : subplot="S"

# Draw Histograms
s.draw(subplot)
 
