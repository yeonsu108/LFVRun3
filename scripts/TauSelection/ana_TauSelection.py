import os
import sys
import ROOT
from ROOT import *
import array

pname = sys.argv[1]
print("pname : " + pname)
outfname = pname + ".root"
outfolder = "./hists/"
if not os.path.isdir(outfolder):
        os.mkdir(outfolder)
print("Output rootfiles will be stored at " + outfolder)

dir_base = "/data1/common/NanoAOD/v8_UL/"
dir_base = "/data1/common/skimmed_NanoAOD/skim_LFVv8/"
dir_input = sys.argv[2]

flist = os.listdir(dir_base + dir_input)
rfile_list = []
conterhist = None

for root, dirs, files in os.walk(dir_base + dir_input):
#    for d in dirs:
#        tmp_files = root + "/" + d + "/*.root"
#        print(tmp_files)
#        rfile_list.append(tmp_files)
    for f in files:
        tmp_file = os.path.join(root,f)
        #print(tmp_file)
        rfile_list.append(tmp_file)

std_rfile_list = ROOT.std.vector('string')()
for r in rfile_list:
    std_rfile_list.push_back(r)

#df = ROOT.RDataFrame("Events",std_rfile_list)
df = ROOT.RDataFrame("outputTree",std_rfile_list)
#
#if pname == "WJetsToLNu_HT-0To100":
#    df = df.Filter("LHE_HT < 100")

#nocutevts = df.Count().GetValue()
#df = df.Filter("HLT_IsoMu24")\
df = df.Define("muoncuts","Muon_pt > 30 && abs(Muon_eta) < 2.4 && Muon_tightId && Muon_pfRelIso04_all < 0.15")\
       .Define("nmuonpass","Sum(muoncuts)")\
       .Define("vetomuoncuts","!muoncuts && Muon_pt > 15 && abs(Muon_eta) < 2.4 && Muon_looseId && Muon_pfRelIso04_all < 0.25")\
       .Define("nvetomuons","Sum(vetomuoncuts)")\
       .Define("vetoelecuts","Electron_pt>15.0 && abs(Electron_eta)<2.4 && Electron_cutBased == 1")\
       .Define("nvetoeles","Sum(vetoelecuts)")\
       .Filter("nmuonpass == 1 && (nvetomuons + nvetoeles) == 0")

df = df.Define("taucuts","Tau_pt>40.0 && abs(Tau_eta)<2.3 && Tau_idDecayModeNewDMs")\
       .Define("deeptauidcuts","Tau_idDeepTau2017v2p1VSmu & 8 && Tau_idDeepTau2017v2p1VSe & 4 && Tau_idDeepTau2017v2p1VSjet & 64")\
       .Define("seltaucuts","taucuts && deeptauidcuts")\
       .Define("ntaupass","Sum(seltaucuts)")\
       .Filter("ntaupass == 1")

hmuon1pt = df.Define("muon1pt","Muon_pt[muoncuts][0]").Histo1D(("hmuon1pt", "hmuon1pt", 40, 0, 400),"muon1pt")
hmuon1eta = df.Define("muon1eta","Muon_eta[muoncuts][0]").Histo1D(("hmuon1eta", "hmuon1eta", 40, -4.0, 4.0),"muon1eta")
htau1pt = df.Define("tau1pt","Tau_pt[seltaucuts][0]").Histo1D(("htau1pt", "htau1pt", 40, 0, 400),"tau1pt")
htau1eta = df.Define("tau1eta","Tau_eta[seltaucuts][0]").Histo1D(("htau1eta", "htau1eta", 40, -4.0, 4.0),"tau1eta")

hfile = TFile( outfolder + outfname, "RECREATE" )
#hcount_nocut = TH1D("hcount_S0","counter",2,0,2)
#hcount_nocut.SetBinContent(1,nocutevts)
#hcount_nocut.Write()
hmuon1pt.Write()
hmuon1eta.Write()
htau1pt.Write()
htau1eta.Write()
hfile.Close()

hcountsum = None
for f in rfile_list:
    infile = ROOT.TFile(f)
    hcount = infile.Get("hcounter_nocut")
    if hcount != None:
        if hcountsum == None:
            hcountsum = hcount.Clone()
            hcountsum.SetDirectory(0)
        else:
            hcountsum.Add(hcount)
    infile.Close()

if hcountsum != None:
    print("Updating with counter histogram")
    outf = ROOT.TFile(outfolder+outfname, "UPDATE")
    hcountsum.Write()
    outf.Write("", ROOT.TObject.kOverwrite)
    outf.Close()
else:
    print("counter histogram not found")

