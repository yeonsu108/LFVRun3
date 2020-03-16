
void ntuplemaker(const char *inputFile)
{
    // Branch Objects
    std::vector<string> obj = {"event"
        ,"nJet","Jet_btagDeepFlavB","Jet_btagDeepFlavC"
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
        ,"nbJet_l","nbJet_m","nbJet_t"
        ,"ncJet_l","ncJet_m","ncJet_t"
        ,"nJet_blcl","nJet_blcm","nJet_blct"
        ,"nJet_bmcl","nJet_bmcm","nJet_bmct"
        ,"nJet_btcl","nJet_btcm","nJet_btct"
    };

    // Get tree from inputFile and make RDF
    ROOT::RDataFrame df("Events",inputFile);

    // Object Selction
    auto sel_Muons = df.Filter("Sum(Muon_pt>30 && abs(Muon_eta)<2.4 && Muon_looseId)==1","Muon selection");
    auto sel_Jets = sel_Muons.Filter("Sum(Jet_pt>30 && abs(Jet_eta)<2.4)>=3","Jet selection");
    auto sel_Taus = sel_Jets.Filter("Sum(Tau_pt>20 && abs(Tau_eta)<2.3 )==1","Tau selection")
                .Define("nbJet_l","Sum(Jet_btagDeepFlavB>0.0494)")
                .Define("nbJet_m","Sum(Jet_btagDeepFlavB>0.2770)")
                .Define("nbJet_t","Sum(Jet_btagDeepFlavB>0.7264)")
                .Define("ncJet_l","Sum((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.4)")
                .Define("ncJet_m","Sum((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.29)")
                .Define("ncJet_t","Sum((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.05)")
                .Define("nJet_blcl","Sum((Jet_btagDeepFlavB>0.0494) && ((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.4000))")
                .Define("nJet_blcm","Sum((Jet_btagDeepFlavB>0.0494) && ((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.2900))")
                .Define("nJet_blct","Sum((Jet_btagDeepFlavB>0.0494) && ((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.0500))")
                .Define("nJet_bmcl","Sum((Jet_btagDeepFlavB>0.2770) && ((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.4000))")
                .Define("nJet_bmcm","Sum((Jet_btagDeepFlavB>0.2770) && ((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.2900))")
                .Define("nJet_bmct","Sum((Jet_btagDeepFlavB>0.2770) && ((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.0500))")
                .Define("nJet_btcl","Sum((Jet_btagDeepFlavB>0.7264) && ((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.4000))")
                .Define("nJet_btcm","Sum((Jet_btagDeepFlavB>0.7264) && ((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.2900))")
                .Define("nJet_btct","Sum((Jet_btagDeepFlavB>0.7264) && ((Jet_btagDeepFlavC/(Jet_btagDeepFlavC+Jet_btagDeepFlavB))>0.0500))");
    
    float nevt_total = df.Count().GetValue();
    float nevt_sel_Muons = sel_Muons.Count().GetValue();
    float nevt_sel_Jets = sel_Jets.Count().GetValue();
    float nevt_sel_Taus = sel_Taus.Count().GetValue();

    cout<<"Total "<<nevt_total<<endl;
    cout<<"S1. Muon Selection "<<nevt_sel_Muons<<endl;
    cout<<"S2. Jet Selection  "<<nevt_sel_Jets<<endl;
    cout<<"S3. Tau Selection "<<nevt_sel_Taus<<endl;
    sel_Taus.Snapshot("tree","output.root",obj);

    TFile f("output.root","UPDATE");
    auto h_cutflow = TH1F("h_cutflow","Cutflow",6,0,6);
    h_cutflow.SetBinContent(1,nevt_total);
    h_cutflow.SetBinContent(2,nevt_sel_Muons);
    h_cutflow.SetBinContent(3,nevt_sel_Jets);
    h_cutflow.SetBinContent(4,nevt_sel_Taus);
    f.Write();
    f.Close();
    
}
