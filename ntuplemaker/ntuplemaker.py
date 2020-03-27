from ROOT import *
import ROOT
import sys

# List of Branch Objects
def objects():
    obj_Event = ['event']
    obj_Jet = ['nJet','Jet_btagDeepFlavB','Jet_btagDeepFlavC','Jet_eta','Jet_mass','Jet_phi','Jet_pt','Jet_cleanmask']
    obj_Electron = ['nElectron','Electron_charge','Electron_eta','Electron_mass','Electron_phi','Electron_pt','Electron_jetIdx','Electron_jetRelIso','Electron_cutBased','Electron_cleanmask']
    obj_Muon = ['nMuon','Muon_charge','Muon_eta','Muon_mass','Muon_phi','Muon_pt','Muon_jetIdx','Muon_jetRelIso','Muon_looseId','Muon_mediumId','Muon_tightId','Muon_cleanmask']
    obj_MET = ['MET_phi','MET_pt','MET_sumEt']
    obj_Tau = ['nTau','Tau_charge','Tau_chargedIso','Tau_eta','Tau_idAntiMu','Tau_mass','Tau_neutralIso','Tau_phi','Tau_pt','Tau_idDeepTau2017v2p1VSe','Tau_idDeepTau2017v2p1VSmu','Tau_idDeepTau2017v2p1VSjet','Tau_jetIdx','Tau_cleanmask','Tau_jetIdx']
    obj_bcJet = ['nbJet_l','nbJet_m','nbJet_t','ncJet_l','ncJet_m','ncJet_t','nJet_blcl','nJet_blcm','nJet_blct','nJet_bmcl','nJet_bmcm','nJet_bmct','nJet_btcl','nJet_btcm','nJet_btct']
    obj = obj_Event + obj_Jet + obj_Electron + obj_Muon + obj_MET + obj_Tau + obj_bcJet
    return obj

# Ntuplemaker RDataFrame
def ntuplemaker(inputfile, obj):
    inputfile = inputfile.replace("\n","")
    df = ROOT.ROOT.RDataFrame("Events", inputfile)

    # Get Branch Lists such as Jet_pt, Muon_eta, ...
    v = ROOT.vector('string')()
    for name in obj:
        v.push_back(name)

    list_cutflow = []
    list_cutflow.append(df.Count().GetValue())  # Total Events

# Jet cut
    cut_Jets = df.Filter('All(Jet_pt > 30 && abs(Jet_eta < 2.4) )','Jet pt & eta cut')
    br_nbJets = cut_Jets.Define('nbJet_l','Sum(Jet_btagDeepFlavB > 0.0494)')  \
                        .Define('nbJet_m','Sum(Jet_btagDeepFlavB > 0.2770)')  \
                        .Define('nbJet_t','Sum(Jet_btagDeepFlavB > 0.7264)')
    br_ncJets = br_nbJets.Define('ncJet_l','Sum(Jet_btagDeepFlavC > 0.03)')  \
                        .Define('ncJet_m','Sum(Jet_btagDeepFlavC > 0.085)')  \
                        .Define('ncJet_t','Sum(Jet_btagDeepFlavC > 0.48)') 
    br_nbcJets = br_ncJets.Define('nJet_blcl','Sum((Jet_btagDeepFlavB > 0.0494) && (Jet_btagDeepFlavC > 0.0300))')  \
                        .Define('nJet_blcm','Sum((Jet_btagDeepFlavB > 0.0494) && (Jet_btagDeepFlavC > 0.0850))')  \
                        .Define('nJet_blct','Sum((Jet_btagDeepFlavB > 0.0494) && (Jet_btagDeepFlavC > 0.4800))')  \
                        .Define('nJet_bmcl','Sum((Jet_btagDeepFlavB > 0.2770) && (Jet_btagDeepFlavC > 0.0300))')  \
                        .Define('nJet_bmcm','Sum((Jet_btagDeepFlavB > 0.2770) && (Jet_btagDeepFlavC > 0.0850))')  \
                        .Define('nJet_bmct','Sum((Jet_btagDeepFlavB > 0.2770) && (Jet_btagDeepFlavC > 0.4800))')  \
                        .Define('nJet_btcl','Sum((Jet_btagDeepFlavB > 0.7264) && (Jet_btagDeepFlavC > 0.0300))')  \
                        .Define('nJet_btcm','Sum((Jet_btagDeepFlavB > 0.7264) && (Jet_btagDeepFlavC > 0.0850))')  \
                        .Define('nJet_btct','Sum((Jet_btagDeepFlavB > 0.7264) && (Jet_btagDeepFlavC > 0.4800))')
    
    list_cutflow.append(cut_Jets.Count().GetValue())  # Jet pt & eta selection

    br_nbcJets.Snapshot('Tree','output.root',v)

    # Add cutflow histogram
    outfile = TFile('output.root','UPDATE')
    h_cutflow = TH1F('h_cutflow','Cutflow',5, 0, 5)
    for i, sel in enumerate(list_cutflow):
        h_cutflow.SetBinContent(i,sel)
    outfile.Write()

inputfile = sys.argv[1]
obj = objects()
ntuplemaker(inputfile, obj)


# Event Selections
#    sel_electron = df.Filter('All(Electron_pt > 30 && abs(Electron_eta) < 2.4)','Electron pt & eta Selection')
#    sel_muon = sel_electron.Filter('All(Muon_pt > 30 && abs(Muon_eta) < 2.4)','Muon pt & eta Selection')
#    #sel_tau = sel_lep_pt.Filter('All(Tau_pt > 30 && (Tau_eta) < 2.4)','Tau pt & eta selection')
#    sel_jet = df.Filter('All(Jet_pt > 30 && abs(Jet_eta < 2.4))','Jet pt & eta Selection')
#    sel_jet_entries = sel_jet.Count()
#    sel_MET = sel_jet.Filter('MET_pt > 30','MET pt Selection')
    
# Add nbjet, ncjet branches
# No Jet cut
#    br_nbcJets = df.Define('nbJet_l','Sum(Jet_btagDeepFlavB > 0.0494)') 
#        .Define('nbJet_m','Sum(Jet_btagDeepFlavB > 0.2770)') 
#        .Define('nbJet_t','Sum(Jet_btagDeepFlavB > 0.7264)') 
#        .Define('ncJet_l','Sum(Jet_btagDeepFlavC > 0.0300)') 
#        .Define('ncJet_m','Sum(Jet_btagDeepFlavC > 0.0850)') 
#        .Define('ncJet_t','Sum(Jet_btagDeepFlavC > 0.4800)')
#        .Define('nJet_blcl','Sum((Jet_btagDeepFlavB > 0.0494) && (Jet_btagDeepFlavC > 0.0300))') 
#        .Define('nJet_blcm','Sum((Jet_btagDeepFlavB > 0.0494) && (Jet_btagDeepFlavC > 0.0850))') 
#        .Define('nJet_blct','Sum((Jet_btagDeepFlavB > 0.0494) && (Jet_btagDeepFlavC > 0.4800))') 
#        .Define('nJet_bmcl','Sum((Jet_btagDeepFlavB > 0.2770) && (Jet_btagDeepFlavC > 0.0300))') 
#        .Define('nJet_bmcm','Sum((Jet_btagDeepFlavB > 0.2770) && (Jet_btagDeepFlavC > 0.0850))') 
#        .Define('nJet_bmct','Sum((Jet_btagDeepFlavB > 0.2770) && (Jet_btagDeepFlavC > 0.4800))') 
#        .Define('nJet_btcl','Sum((Jet_btagDeepFlavB > 0.7264) && (Jet_btagDeepFlavC > 0.0300))') 
#        .Define('nJet_btcm','Sum((Jet_btagDeepFlavB > 0.7264) && (Jet_btagDeepFlavC > 0.0850))') 
#        .Define('nJet_btct','Sum((Jet_btagDeepFlavB > 0.7264) && (Jet_btagDeepFlavC > 0.4800))') 


#files = rs.rootfiles(year, sample)  # year : 2016, ... sample : DoubleEG, ...
#print(len(files))
#for i,inputfile in enumerate(files):         # Each run contains upto 20 rootfiles
#    #inputfile = ROOT.vector('string')()
#    print(str(i) +"th Run of "+ year + sample)
#    #for name in files[i]:
#    #    inputfile.push_back(name)
#    outputfilename = "Data_Run" + year + "_" + sample + "_" + str(i) + ".root"
#    outputfile = "./ntuples/data_Run" + year + sample + "/" + outputfilename
#    ntuplemaker(inputfile, outputfile)



## Object Selections
#sel_obj_1l = sel_MET.Filter('nElectron + nMuon == 1','Number of Leptons = 1')
#
## Obj Selection 1
#sel_obj_3j = sel_obj_1l.Filter('nJet >= 3','Number of Jets >= 3')
#sel_obj_1tau = sel_obj_3j.Filter('nTau == 1','Number of Tau == 1')
#
## Obj Selection 2 and 3
#sel_obj_2j = sel_obj_1l.Filter('nJet >= 2','Number of Jets >= 2')
#sel_obj_1b = sel_obj_2j.Filter('nbJet == 1','One b-tagged jet')
#
## Save ntuples to outputfile
#sel_obj_1tau.Snapshot(treename, out_sel1, v)
#sel_obj_1b.Snapshot(treename, out_sel2, v)
#
#report1 = sel_obj_1tau.Report()
#report2 = sel_obj_1b.Report()
#
#print("\n1tau")
#report1.Print()
#print("\n1bjet")
#report2.Print()


#report = sel_jet_pt.Report()

#sel_MET_pt.Snapshot(treename, outputfile, v)

#report = sel_MET_pt.Report()
#report.Print()

#h_nJet = ''' "nJet", "nJet", 15, 0, 15 '''
#h_nMuon = ''' "nMuon", "nMuon", 5, 0, 5 '''
#h_nElectron = ''' "nElectron", "nElectron", 5, 0, 5 '''
#h_Jet_pt = ''' "Jet_pt", "Jet_pt", 25, 0, 500 '''
#h_Jet_eta = ''' "Jet_eta", "Jet_eta", 20, 0, 4.0 '''
#h_Jet_phi = ''' "Jet_phi", "Jet_phi", 20, -4.0, 4.0 '''

#hist = []
#for i, name in enumerate(objects):
#    hist[i] = df_sel.Histo1D((


