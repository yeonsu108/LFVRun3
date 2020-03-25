
void ntuplemaker(const char *inputFile)
{
    // Branch Objects
    std::vector<string> obj = {"event"
        ,"nJet","Jet_btagDeepB","Jet_btagDeepC"
        ,"Jet_eta","Jet_mass","Jet_phi","Jet_pt","Jet_cleanmask"
        ,"nElectron","Electron_charge","Electron_eta"
        ,"Electron_mass","Electron_phi","Electron_pt"
        ,"Electron_jetIdx","Electron_jetRelIso"
        ,"Electron_cutBased","Electron_cleanmask"
        ,"nMuon","Muon_charge","Muon_eta"
        ,"Muon_mass","Muon_phi","Muon_pt"
        ,"Muon_jetIdx","Muon_jetRelIso"
        ,"Muon_looseId","Muon_mediumId"
        ,"Muon_tightId","Muon_cleanmask"
        ,"MET_phi","MET_pt","MET_sumEt"
        ,"nTau","Tau_charge","Tau_chargedIso","Tau_eta"
        ,"Tau_idAntiMu","Tau_mass","Tau_neutralIso"
        ,"Tau_phi","Tau_pt","Tau_idDeepTau2017v2p1VSe"
        ,"Tau_idDeepTau2017v2p1VSmu","Tau_idDeepTau2017v2p1VSjet"
        ,"Tau_jetIdx","Tau_cleanmask","Tau_jetIdx"
        ,"HLT_IsoMu24"
    };

    // Get tree from inputFile and make RDF
    ROOT::RDataFrame df("Events",inputFile);
    float nevt_total = df.Count().GetValue();

    // Selction & Histogram

    auto trg_hlt = df.Filter("HLT_IsoMu24","SingleMuon HLT");
    float nevt_trg_hlt = trg_hlt.Count().GetValue();

    // Muon Selection //
    auto sel_Muons = trg_hlt.Filter("Sum(Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_tightId) >= 1","Muon selection");
    float nevt_sel_Muons = sel_Muons.Count().GetValue();

    // Tau Selection //
    auto sel_Taus = sel_Muons.Filter("Sum(Tau_pt>50 && abs(Tau_eta)<2.3 && Tau_idDeepTau2017v2p1VSjet & 8 &&  Tau_idDeepTau2017v2p1VSe & 8 &&  Tau_idDeepTau2017v2p1VSmu & 8) == 1","Tau selection");
    float nevt_sel_Taus = sel_Taus.Count().GetValue();
    
    // Jet Selection //
    auto sel_Jets = sel_Taus.Filter("Sum(Jet_pt>30 && abs(Jet_eta)<2.4) >= 3","Jet selection");
    float nevt_sel_Jets = sel_Jets.Count().GetValue();


    // Histograms
    auto h_nTau = sel_Jets.Histo1D({"h_nTau","Number of Taus",4,0,4},"nTau");https://youtu.be/ynEOo28lsbc
    auto h_nMuon = sel_Jets.Histo1D({"h_nMuon","Number of Muons",7,0,7},"nMuon");
    auto h_nJet = sel_Jets.Histo1D({"h_nJet","Number of Jets",20,0,20},"nJet");
    
    // 2016
    auto h_nbJet_l = sel_Jets.Define("nbJet_l","Sum(Jet_btagDeepB>0.0614)").Histo1D({"h_nbJet_l","Loose bJets",7,0,7},"nbJet_l");
    auto h_nbJet_m = sel_Jets.Define("nbJet_m","Sum(Jet_btagDeepB>0.3093)").Histo1D({"h_nbJet_m","Medium bJets",7,0,7},"nbJet_m");
    auto h_nbJet_t = sel_Jets.Define("nbJet_t","Sum(Jet_btagDeepB>0.7221)").Histo1D({"h_nbJet_t","Tight bJets",7,0,7},"nbJet_t");
    // 2017
    //auto h_nbJet_l = sel_Jets.Define("nbJet_l","Sum(Jet_btagDeepB>0.1522)").Histo1D({"h_nbJet_l","Loose bJets",7,0,7},"nbJet_l");
    //auto h_nbJet_m = sel_Jets.Define("nbJet_m","Sum(Jet_btagDeepB>0.4941)").Histo1D({"h_nbJet_m","Medium bJets",7,0,7},"nbJet_m");
    //auto h_nbJet_t = sel_Jets.Define("nbJet_t","Sum(Jet_btagDeepB>0.8001)").Histo1D({"h_nbJet_t","Tight bJets",7,0,7},"nbJet_t");
    // 2018
    //auto h_nbJet_l = sel_Jets.Define("nbJet_l","Sum(Jet_btagDeepB>0.1241)").Histo1D({"h_nbJet_l","Loose bJets",7,0,7},"nbJet_l");
    //auto h_nbJet_m = sel_Jets.Define("nbJet_m","Sum(Jet_btagDeepB>0.4184)").Histo1D({"h_nbJet_m","Medium bJets",7,0,7},"nbJet_m");
    //auto h_nbJet_t = sel_Jets.Define("nbJet_t","Sum(Jet_btagDeepB>0.7527)").Histo1D({"h_nbJet_t","Tight bJets",7,0,7},"nbJet_t");
    auto h_goodMuon_pt = sel_Jets.Define("goodMuon_pt","Muon_pt[ (Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_tightId) ]").Histo1D({"h_goodMuon_pt","Muon pt",20,0,400},"goodMuon_pt");
    auto h_goodJet_pt = sel_Jets.Define("goodJet_pt","Jet_pt[ (Jet_pt>30 && abs(Jet_eta)<2.4) ]").Histo1D({"h_goodJet_pt","Jet pt",20,0,400},"goodJet_pt");
    auto h_goodTau_pt = sel_Jets.Define("goodTau_pt","Tau_pt[ (Tau_pt>50 && abs(Tau_eta)<2.3 && Tau_pt>50 && abs(Tau_eta)<2.3 && Tau_idDeepTau2017v2p1VSjet & 16 &&  Tau_idDeepTau2017v2p1VSe & 16 &&  Tau_idDeepTau2017v2p1VSmu & 16) ]").Histo1D({"h_goodTau_pt","Tau pt",20,0,400},"goodTau_pt");
    auto h_goodMuon_eta = sel_Jets.Define("goodMuon_eta","Muon_eta[ (Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_tightId) ]").Histo1D({"h_goodMuon_eta","Muon eta",20,-4,4},"goodMuon_eta");
    auto h_goodTau_eta = sel_Jets.Define("goodTau_eta","Tau_eta[ (Tau_pt>50 && abs(Tau_eta)<2.3 && Tau_pt>50 && abs(Tau_eta)<2.3 && Tau_idDeepTau2017v2p1VSjet & 16 &&  Tau_idDeepTau2017v2p1VSe & 16 &&  Tau_idDeepTau2017v2p1VSmu & 16) ]").Histo1D({"h_goodTau_eta","Tau eta",20,-4,4},"goodTau_eta");
    auto h_goodJet_eta = sel_Jets.Define("goodJet_eta","Jet_eta[ (Jet_pt>30 && abs(Jet_eta)<2.4) ]").Histo1D({"h_goodJet_eta","Jet eta",20,-4,4},"goodJet_eta");
    
    cout<<"Total "<<nevt_total<<endl;
    cout<<"Trigger "<<nevt_trg_hlt<<endl;
    cout<<"S1. Muon Selection "<<nevt_sel_Muons<<endl;
    cout<<"S2. Tau Selection "<<nevt_sel_Taus<<endl;
    cout<<"S3. Jet Selection  "<<nevt_sel_Jets<<endl;

    // Histogram

    sel_Jets.Snapshot("tree","output.root",obj);

    TFile f("output.root","UPDATE");
    auto h_cutflow = TH1F("h_cutflow","Cutflow",7,0,7);
    h_cutflow.SetBinContent(1,nevt_total);
    h_cutflow.SetBinContent(2,nevt_trg_hlt);
    h_cutflow.SetBinContent(3,nevt_sel_Muons);
    h_cutflow.SetBinContent(4,nevt_sel_Taus);
    h_cutflow.SetBinContent(5,nevt_sel_Jets);
    h_nMuon->Write();
    h_nTau->Write();
    h_nJet->Write();
    h_nbJet_l->Write();
    h_nbJet_m->Write();
    h_nbJet_t->Write();
    h_goodMuon_pt->Write();
    h_goodMuon_eta->Write();
    h_goodTau_pt->Write();
    h_goodTau_eta->Write();
    h_goodJet_pt->Write();
    h_goodJet_eta->Write();
    f.Write();
    f.Close();
    
}
