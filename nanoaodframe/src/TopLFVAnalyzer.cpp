/*
 * TopLFVAnalyzer.cpp
 *
 *  Created on: April 9, 2020
 *      Author: Tae Jeong Kim
 */

#include "TopLFVAnalyzer.h"
#include "utility.h"

TopLFVAnalyzer::TopLFVAnalyzer(TTree *t, std::string outfilename, std::string year, std::string syst, std::string jsonfname, string globaltag, int nthreads)
:NanoAODAnalyzerrdframe(t, outfilename, year, syst, jsonfname, globaltag, nthreads), _syst(syst), _year(year)
{
    if(syst.find("jes") != std::string::npos or syst.find("jes") != std::string::npos or
            syst.find("tes") != std::string::npos or syst.find("hdamp") != std::string::npos or syst.find("tune") != std::string::npos) {
        ext_syst = true;
    }
    _syst = syst;
}

// Define your cuts here
void TopLFVAnalyzer::defineCuts() {

    addCuts("nmuonpass == 1 && nvetoelepass == 0 && nvetomuons == 0","0");
    addCuts("ncleantaupass == 1", "00");
    addCuts("mutau_charge < 0", "000");
    addCuts("ncleanjetspass >= 3", "0000");
    addCuts("ncleanbjetspass == 1", "00000");
    // Control Region
    //addCuts("ncleanbjetspass > 1", "00000");
}

void TopLFVAnalyzer::defineMoreVars() {

    defineVar("muonvec", ::select_leadingvec, {"muon4vecs"});
    defineVar("tauvec", ::select_leadingvec, {"cleantau4vecs"});
    defineVar("mutau_mass",::calculate_invMass,{"muonvec","tauvec"});
    defineVar("mutau_dEta",::calculate_deltaEta,{"muonvec","tauvec"});
    defineVar("mutau_dPhi",::calculate_deltaPhi,{"muonvec","tauvec"});
    defineVar("mutau_dR",::calculate_deltaR,{"muonvec","tauvec"});
    defineVar("muMET_mt",::calculate_MT,{"muon4vecs","MET_pt","MET_phi"});

    // Already object selection is done before this
    // There should be 'good' tau (or none) and exactly one muon
    addVar({"Muon1_pt", "Muon_pt[0]", ""});
    addVar({"Muon1_eta", "Muon_eta[0]", ""});
    addVar({"Muon1_mass", "Muon_mass[0]", ""});
    addVar({"Muon1_charge", "Muon_charge[0]", ""});

    addVar({"Tau1_pt", "Tau_pt[0]", ""});
    addVar({"Tau1_eta", "Tau_eta[0]", ""});
    addVar({"Tau1_mass", "Tau_mass[0]", ""});
    addVar({"Tau1_charge", "Tau_charge[0]", ""});

    addVar({"mutau_charge", "Muon1_charge * Tau1_charge", ""});

    addVar({"Jet1_pt", "(Jet_pt.size()>0) ? Jet_pt[0] : -1", ""});
    addVar({"Jet1_eta", "Jet_eta[0]", ""});
    addVar({"Jet1_mass", "Jet_mass[0]", ""});
    addVar({"Jet1_btagDeepFlavB","Jet_btagDeepFlavB[0]",""});

    addVar({"Jet2_pt", "Jet_pt[1]", ""});
    addVar({"Jet2_eta", "Jet_eta[1]", ""});
    addVar({"Jet2_mass", "Jet_mass[1]", ""});
    addVar({"Jet2_btagDeepFlavB","Jet_btagDeepFlavB[1]",""});

    addVar({"Jet3_pt", "Jet_pt[2]", ""});
    addVar({"Jet3_eta", "Jet_eta[2]", ""});
    addVar({"Jet3_mass", "Jet_mass[2]", ""});
    addVar({"Jet3_btagDeepFlavB","Jet_btagDeepFlavB[2]",""});


    addVar({"bJet1_pt", "bJet_pt[0]", ""});
    addVar({"bJet1_eta", "bJet_eta[0]", ""});
    addVar({"bJet1_mass", "bJet_mass[0]", ""});

    // Reconstruction
//    defineVar("top_reco_whad", ::top_reconstruction_STLFV, {"cleanjet4vecs","cleanbjet4vecs","muon4vecs","cleantau4vecs"});
//    addVar({"chi2","top_reco_whad[0]",""});
//    addVar({"chi2_SMW_mass","top_reco_whad[1]",""});
//    addVar({"chi2_SMTop_mass","top_reco_whad[2]",""});
//    addVar({"chi2_wjet1_idx","top_reco_whad[3]",""});
//    addVar({"chi2_wjet2_idx","top_reco_whad[4]",""});
//    addVar({"chi2_SMW","top_reco_whad[5]",""});
//    addVar({"chi2_SMTop","top_reco_whad[6]",""});
//
//    defineVar("top_reco_prod", ::top_reco_products_STLFV, {"cleanjet4vecs","muon4vecs","cleantau4vecs","top_reco_whad"});
//    addVar({"chi2_wqq_dEta","top_reco_prod[0]",""});
//    addVar({"chi2_wqq_dPhi","top_reco_prod[1]",""});
//    addVar({"chi2_wqq_dR","top_reco_prod[2]",""});
//

    // EventWeights
    // Calculate product of weights and store for systematic study
    // External systs: JES (+btag) (14), JER(2), TES(2), hdamp(2), TuneCP5(2)
    // Weights systs: genWeight(1), PU(2), btag(16), muon Id(2)/Iso(2)/Trg(2), tauId(2*2*2), ME scale(6), PS scale(4), PDF(102)
    // Not implemented: EEprefire, top pt reweighting,

    if (_syst == "data") {
        addVar({"eventWeight", "1.0"});
    } else {
        addVar({"eventWeight__genpu", "unitGenWeight * puWeight[0]"});
        addVar({"eventWeight__mu", "muonWeightId[0] * muonWeightIso[0] * muonWeightTrg[0]"});
        addVar({"eventWeight__tau", "tauWeightIdVsJet[0][0] * tauWeightIdVsEl[0][0] * tauWeightIdVsMu[0][0]"});
        addVar({"eventWeight__nopu", "unitGenWeight * eventWeight__mu * eventWeight__tau * btagWeight_DeepFlavB[0]"});
        addVar({"eventWeight__nobtag", "eventWeight__genpu * eventWeight__mu * eventWeight__tau"});

        if (_syst == "" or ext_syst) {
            // for external syst, we only need nominal weight
            addVar({"eventWeight", "eventWeight__genpu * eventWeight__mu * eventWeight__tau * btagWeight_DeepFlavB[0]"});
        } else {
            addVar({"eventWeight", "eventWeight__genpu * eventWeight__mu * eventWeight__tau * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__puup", "unitGenWeight * puWeight[1] * eventWeight__mu * eventWeight__tau * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__pudown", "unitGenWeight * puWeight[2] * eventWeight__mu * eventWeight__tau * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__muidup", "eventWeight__genpu * muonWeightId[1] * muonWeightIso[0] * muonWeightTrg[0] * eventWeight__tau * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__muiddown", "eventWeight__genpu * muonWeightId[2] * muonWeightIso[0] * muonWeightTrg[0] * eventWeight__tau * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__muisoup", "eventWeight__genpu * muonWeightId[0] * muonWeightIso[1] * muonWeightTrg[0] * eventWeight__tau * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__muisodown", "eventWeight__genpu * muonWeightId[0] * muonWeightIso[2] * muonWeightTrg[0] * eventWeight__tau * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__mutrgup", "eventWeight__genpu * muonWeightId[0] * muonWeightIso[0] * muonWeightTrg[1] * eventWeight__tau * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__mutrgdown", "eventWeight__genpu * muonWeightId[0] * muonWeightIso[0] * muonWeightTrg[2] * eventWeight__tau * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__tauidjetup", "eventWeight__genpu * eventWeight__mu * tauWeightIdVsJet[0][1] * tauWeightIdVsEl[0][0] * tauWeightIdVsMu[0][0] * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__tauidjetdown", "eventWeight__genpu * eventWeight__mu * tauWeightIdVsJet[0][2] * tauWeightIdVsEl[0][0] * tauWeightIdVsMu[0][0] * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__tauidelup", "eventWeight__genpu * eventWeight__mu * tauWeightIdVsJet[0][0] * tauWeightIdVsEl[0][1] * tauWeightIdVsMu[0][0] * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__tauideldown", "eventWeight__genpu * eventWeight__mu * tauWeightIdVsJet[0][0] * tauWeightIdVsEl[0][2] * tauWeightIdVsMu[0][0] * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__tauidmuup", "eventWeight__genpu * eventWeight__mu * tauWeightIdVsJet[0][0] * tauWeightIdVsEl[0][0] * tauWeightIdVsMu[0][1] * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__tauidmudown", "eventWeight__genpu * eventWeight__mu * tauWeightIdVsJet[0][0] * tauWeightIdVsEl[0][0] * tauWeightIdVsMu[0][2] * btagWeight_DeepFlavB[0]"});
            addVar({"eventWeight__btaghfup", "eventWeight__nobtag * btagWeight_DeepFlavB[1]"});
            addVar({"eventWeight__btaghfdown", "eventWeight__nobtag * btagWeight_DeepFlavB[2]"});
            addVar({"eventWeight__btaglfup", "eventWeight__nobtag * btagWeight_DeepFlavB[3]"});
            addVar({"eventWeight__btaglfdown", "eventWeight__nobtag * btagWeight_DeepFlavB[4]"});
            addVar({"eventWeight__btaghfstats1up", "eventWeight__nobtag * btagWeight_DeepFlavB[5]"});
            addVar({"eventWeight__btaghfstats1down", "eventWeight__nobtag * btagWeight_DeepFlavB[6]"});
            addVar({"eventWeight__btaghfstats2up", "eventWeight__nobtag * btagWeight_DeepFlavB[7]"});
            addVar({"eventWeight__btaghfstats2down", "eventWeight__nobtag * btagWeight_DeepFlavB[8]"});
            addVar({"eventWeight__btaglfstats1up", "eventWeight__nobtag * btagWeight_DeepFlavB[9]"});
            addVar({"eventWeight__btaglfstats1down", "eventWeight__nobtag * btagWeight_DeepFlavB[10]"});
            addVar({"eventWeight__btaglfstats2up", "eventWeight__nobtag * btagWeight_DeepFlavB[11]"});
            addVar({"eventWeight__btaglfstats2down", "eventWeight__nobtag * btagWeight_DeepFlavB[12]"});
            addVar({"eventWeight__btagcferr1up", "eventWeight__nobtag * btagWeight_DeepFlavB[13]"});
            addVar({"eventWeight__btagcferr1down", "eventWeight__nobtag * btagWeight_DeepFlavB[14]"});
            addVar({"eventWeight__btagcferr2up", "eventWeight__nobtag * btagWeight_DeepFlavB[15]"});
            addVar({"eventWeight__btagcferr2down", "eventWeight__nobtag * btagWeight_DeepFlavB[16]"});

            if (_syst == "theory") {
                // ME: [0] is renscfact=0.5d0 facscfact=0.5d0 ; [1] is renscfact=0.5d0 facscfact=1d0 ; [3] is renscfact=1d0 facscfact=0.5d0 ;
                //     [5] is renscfact=1d0 facscfact=2d0 ; [7] is renscfact=2d0 facscfact=1d0 ; [8] is renscfact=2d0 facscfact=2d0
                addVar({"eventWeight__scale0", "eventWeight * LHEScaleWeight[0]"});
                addVar({"eventWeight__scale1", "eventWeight * LHEScaleWeight[1]"});
                addVar({"eventWeight__scale2", "eventWeight * LHEScaleWeight[3]"});
                addVar({"eventWeight__scale3", "eventWeight * LHEScaleWeight[5]"});
                addVar({"eventWeight__scale4", "eventWeight * LHEScaleWeight[7]"});
                addVar({"eventWeight__scale5", "eventWeight * LHEScaleWeight[8]"});
                // PS: [0] is ISR=2 FSR=1; [1] is ISR=1 FSR=2[2] is ISR=0.5 FSR=1; [3] is ISR=1 FSR=0.5;
                addVar({"eventWeight__ps0", "eventWeight * PSWeight[0]"});
                addVar({"eventWeight__ps1", "eventWeight * PSWeight[1]"});
                addVar({"eventWeight__ps2", "eventWeight * PSWeight[2]"});
                addVar({"eventWeight__ps3", "eventWeight * PSWeight[3]"});
                // PDF: LHA IDs 306000 - 306102. 306000 = nominal.
                // TODO Check if always 103 entries are stored. unless code will crash.
                for (int i=1; i<=102; i++) {
                    addVar({"eventWeight__pdf" + std::to_string(i), "eventWeight * LHEPdfWeight[" + std::to_string(i) + "]"});
                }
            }
        }
    }

    // define variables that you want to store
    addVartoStore("run");
    addVartoStore("event");
    addVartoStore("eventWeight.*");
    addVartoStore("nmuonpass");
    addVartoStore("ncleanjetspass");
    addVartoStore("ncleanbjetspass");
    addVartoStore("ncleantaupass");
    addVartoStore("Jet1_.*");
    addVartoStore("Jet2_.*");
    addVartoStore("Jet3_.*");
    addVartoStore("bJet1_.*");
    addVartoStore("Tau1.*");
    addVartoStore("Muon1.*");
    addVartoStore("mutau.*");
    addVartoStore("MET.*");
//    addVartoStore("chi2.*");
    addVartoStore("btagWeight_DeepFlavB");
    addVartoStore("eventWeight.*");
}

void TopLFVAnalyzer::bookHists() {

    std::vector<std::string> init_weight = {""};
    std::vector<std::string> sf_weight = {"", "__nobtag", "__nopu", "__puup", "__pudown",
                   "__muidup", "__muiddown", "__muisoup", "__muisodown", "__mutrgup", "__mutrgdown",
                   "__tauidjetup", "__tauidjetdown", "__tauidelup", "__tauideldown", "__tauidmuup", "__tauidmudown", 
                   "__btaghfup", "__btaghfdown", "__btaglfup", "__btaglfdown",
                   "__btaghfstats1up", "__btaghfstats1down", "__btaghfstats2up", "__btaghfstats2down",
                   "__btaglfstats1up", "__btaglfstats1down", "__btaglfstats2up", "__btaglfstats2down",
                   "__btagcferr1up", "__btagcferr1down", "__btagcferr2up", "__btagcferr2down"};

    std::vector<std::string> theory_weight = {"__ps0", "__ps1", "__ps2", "__ps3",
          "__scale0", "__scale1", "__scale2", "__scale3", "__scale4", "__scale5",
          "__pdf1", "__pdf2", "__pdf3", "__pdf4", "__pdf5",
          "__pdf6", "__pdf7", "__pdf8", "__pdf9", "__pdf10",
          "__pdf11", "__pdf12", "__pdf13", "__pdf14", "__pdf15",
          "__pdf16", "__pdf17", "__pdf18", "__pdf19", "__pdf20",
          "__pdf21", "__pdf22", "__pdf23", "__pdf24", "__pdf25",
          "__pdf26", "__pdf27", "__pdf28", "__pdf29", "__pdf30",
          "__pdf31", "__pdf32", "__pdf33", "__pdf34", "__pdf35",
          "__pdf36", "__pdf37", "__pdf38", "__pdf39", "__pdf40",
          "__pdf41", "__pdf42", "__pdf43", "__pdf44", "__pdf45",
          "__pdf46", "__pdf47", "__pdf48", "__pdf49", "__pdf50",
          "__pdf51", "__pdf52", "__pdf53", "__pdf54", "__pdf55",
          "__pdf56", "__pdf57", "__pdf58", "__pdf59", "__pdf60",
          "__pdf61", "__pdf62", "__pdf63", "__pdf64", "__pdf65",
          "__pdf66", "__pdf67", "__pdf68", "__pdf69", "__pdf70",
          "__pdf71", "__pdf72", "__pdf73", "__pdf74", "__pdf75",
          "__pdf76", "__pdf77", "__pdf78", "__pdf79", "__pdf80",
          "__pdf81", "__pdf82", "__pdf83", "__pdf84", "__pdf85",
          "__pdf86", "__pdf87", "__pdf88", "__pdf89", "__pdf90",
          "__pdf91", "__pdf92", "__pdf93", "__pdf94", "__pdf95",
          "__pdf96", "__pdf97", "__pdf98", "__pdf99", "__pdf100",
          "__pdf101", "__pdf102"};

    // TODO refine this
    std::vector<std::string> syst_weight;
    if (_syst == "" or _syst == "nosyst" or _syst == "data" or ext_syst) syst_weight = init_weight;
    else {
        syst_weight = sf_weight;
        if (_syst == "theory") syst_weight.insert(syst_weight.end(), theory_weight.begin(),  theory_weight.end());
    }

    cout << "Variations to take care :";
    for (auto i : syst_weight) cout << i << " ";
    cout << endl;

    for (std::string weightstr : syst_weight) {
        add1DHist({"h_nevents", "Number of Events", 2, -0.5, 1.5}, "one", "eventWeight", weightstr, "0");
        add1DHist({"h_nvtx", "Number of Primary Vertex", 100, 0.0, 100.0}, "PV_npvsGood", "eventWeight", weightstr, "0");

        add1DHist({"h_met_pt", "MET pt", 20, 0, 400}, "MET_pt", "eventWeight", weightstr, "0");
        add1DHist({"h_sum_et", "Sum ET", 50, 0.0, 5000.0}, "MET_sumEt", "eventWeight", weightstr, "0");
        add1DHist({"h_met_phi", "MET phi", 20, -3.2, 3.2}, "MET_phi", "eventWeight", weightstr, "0");

        add1DHist({"h_nmuonpass", "Passing muoncuts", 5, 0.0, 5.0}, "nmuonpass", "eventWeight", weightstr, "0");
        add1DHist({"h_ncleantaupass", "Passing taucuts", 5, 0.0, 5.0}, "ncleantaupass", "eventWeight", weightstr, "0");
        add1DHist({"h_ncleanjetspass", "Passing jetcuts", 10, 0.0, 10.0}, "ncleanjetspass", "eventWeight", weightstr, "0");
        add1DHist({"h_ncleanbjetspass", "Passing bjetcuts", 5, 0.0, 5.0}, "ncleanbjetspass", "eventWeight", weightstr, "0");

        add1DHist({"h_muon1_pt", "Muon pt", 30, 0, 600}, "Muon1_pt", "eventWeight", weightstr, "0");
        add1DHist({"h_muon1_eta", "Muon eta", 20, -2.5, 2.5}, "Muon1_eta", "eventWeight", weightstr, "0");
        add1DHist({"h_muMET_mt", "Muon met mt", 20, 0, 400}, "muMET_mt", "eventWeight", weightstr, "0");

        add1DHist({"h_tau1_pt", "Tau pt", 20, 0, 400}, "Tau1_pt", "eventWeight", weightstr, "0");
        add1DHist({"h_tau1_eta", "Tau eta", 20, -2.5, 2.5}, "Tau1_eta", "eventWeight", weightstr, "0");
        add1DHist({"h_tau1_mass", "Tau mass", 20, 0, 100}, "Tau1_mass", "eventWeight", weightstr, "0");

        add1DHist({"h_mutau_dEta", "dEta of muon and tau", 25, -5, 5}, "mutau_dEta", "eventWeight", weightstr, "00");
        add1DHist({"h_mutau_dPhi", "dPhi of muon and tau", 20, -3.2, 3.2}, "mutau_dPhi", "eventWeight", weightstr, "00");
        add1DHist({"h_mutau_dR", "dR of muon and tau", 20, 0, 4.0}, "mutau_dR", "eventWeight", weightstr, "00");
        add1DHist({"h_mutau_mass", "Mass of muon and tau", 40, 0, 1000}, "mutau_mass", "eventWeight", weightstr, "00");

        add1DHist({"h_jet1_pt", "leading jet pt", 20, 0, 400}, "Jet1_pt", "eventWeight", weightstr, "0");
        add1DHist({"h_jet1_eta", "leading jet eta", 20, -2.5, 2.5}, "Jet1_eta", "eventWeight", weightstr, "0");
        add1DHist({"h_jet1_mass", "leading jet mass", 20, 0, 100}, "Jet1_mass", "eventWeight", weightstr, "0");
        add1DHist({"h_jet1_btag","btag discr of leading jet", 20, 0, 1.0}, "Jet1_btagDeepFlavB", "eventWeight", weightstr, "0");

        add1DHist({"h_jet2_pt", "sub-leading jet pt", 20, 0, 400}, "Jet2_pt", "eventWeight", weightstr, "0000");
        add1DHist({"h_jet2_eta", "sub-leading jet eta", 20, -2.5, 2.5}, "Jet2_eta", "eventWeight", weightstr, "0000");
        add1DHist({"h_jet2_mass", "sub-leading jet mass", 20, 0, 100}, "Jet2_mass", "eventWeight", weightstr, "0000");
        add1DHist({"h_jet2_btag","btag discr of sub-leading jet", 20, 0, 1.0}, "Jet2_btagDeepFlavB", "eventWeight", weightstr, "0000");

        add1DHist({"h_jet3_pt", "third jet pt", 20, 0, 400}, "Jet3_pt", "eventWeight", weightstr, "0000");
        add1DHist({"h_jet3_eta", "third jet eta", 20, -2.5, 2.5}, "Jet3_eta", "eventWeight", weightstr, "0000");
        add1DHist({"h_jet3_mass", "third jet mass", 20, 0, 100}, "Jet3_mass", "eventWeight", weightstr, "0000");
        add1DHist({"h_jet3_btag","btag discr of third jet", 20, 0, 1.0}, "Jet3_btagDeepFlavB", "eventWeight", weightstr, "0000");

        add1DHist({"h_bjet1_pt", "b jet pt", 20, 0, 400}, "bJet1_pt", "eventWeight", weightstr, "00000");
        add1DHist({"h_bjet1_eta", "b jet eta", 20, -2.5, 2.5}, "bJet1_eta", "eventWeight", weightstr, "00000");
        add1DHist({"h_bjet1_mass", "b jet mass", 20, 0, 100}, "bJet1_mass", "eventWeight", weightstr, "00000");
    }

//    // Histogram of Top mass reconstruction
//    add1DHist({"h_chi2", "Minimum chi2 for hadronic W", 20, 0, 1000}, "chi2", "eventWeight","00000");
//    add1DHist({"h_chi2_SMTop_mass", "chi2 SM Top mass", 20, 0, 400}, "chi2_SMTop_mass", "eventWeight","00000");
//    add1DHist({"h_chi2_SMW_mass", "chi2 SM W mass", 20, 0, 400}, "chi2_SMW_mass", "eventWeight","00000");
//    add1DHist({"h_chi2_wqq_dEta", "dEta of jets from W", 25, -5, 5}, "chi2_wqq_dEta", "eventWeight","00000");
//    add1DHist({"h_chi2_wqq_dPhi", "dPhi of jets from W", 20, -4, 4}, "chi2_wqq_dPhi", "eventWeight","00000");
//    add1DHist({"h_chi2_wqq_dR", "dR of jets from W", 20, 0, 4.0}, "chi2_wqq_dR", "eventWeight","00000");
}
