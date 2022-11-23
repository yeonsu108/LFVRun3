/*
 * NanoAODAnalyzerrdframe.cpp
 *
 *  Created on: Sep 30, 2018
 *      Author: suyong
 *      Refactored for LFV analysis: jiwon park
 */

#include "NanoAODAnalyzerrdframe.h"
#include <iostream>
#include <algorithm>
#include <typeinfo>

#include "TCanvas.h"
#include "Math/GenVector/VectorUtil.h"
#include <vector>
#include <fstream>
#include "utility.h"
#include <regex>
#include "ROOT/RDFHelpers.hxx"
#include "correction.h"

using namespace std;

NanoAODAnalyzerrdframe::NanoAODAnalyzerrdframe(TTree *atree, std::string outfilename, std::string year, std::string syst, std::string jsonfname, std::string globaltag, int nthreads)
:_rd(*atree), _isData(false), _jsonOK(false), _outfilename(outfilename), _year(year), _syst(syst), _jsonfname(jsonfname), _globaltag(globaltag), _inrootfile(0), _outrootfile(0), _rlm(_rd), _rnt(&_rlm), currentnode(0), _jetCorrector(0) {

    // Skim switch
    if (_isSkim == true) {
        cout << "<< Start Skim NanoAOD >>" << endl;
    } else {
        cout << "<< Start Process NanoAOD >>" << endl;
    }

    // Year switch
    if (_year.find("2016pre") != std::string::npos) {
        _isRun16pre = true;
        cout << "Year : Run 2016 pre (16 APV)" << endl;
    } else if (_year.find("2016post") != std::string::npos) {
        _isRun16post = true;
        cout << "Year : Run 2016 post" << endl;
    } else if (_year.find("2017") != std::string::npos) {
        _isRun17 = true;
        cout << "Year : Run 2017" << endl;
    } else if (_year.find("2018") != std::string::npos) {
        _isRun18 = true;
        cout << "Year : Run 2018" << endl;
    }
    _isRun16 = _isRun16pre || _isRun16post;

    // Data/mc switch
    if (atree->GetBranch("genWeight") == nullptr) {
        _isData = true;
        cout << "Input file is data" <<endl;
    } else {
        _isData = false;
        cout << "Input file is MC" <<endl;
    }

    // Systematic switch
    if (_syst != "") {
        cout << "Systematics Information" << endl;
        cout << "Activated option --syst " << _syst << endl;
        if (_syst.find("jes") != std::string::npos) {
            _isSystJes = true;
            cout << "    Apply JES uncertainty" << endl;
        }
    } else {
        cout << "Nominal process without systematics" << endl;
    }

    TObjArray *allbranches = atree->GetListOfBranches();
    for (int i =0; i<allbranches->GetSize(); i++) {
        TBranch *abranch = dynamic_cast<TBranch *>(allbranches->At(i));
        if (abranch!= nullptr) {
            std::string brname = abranch->GetName();
            if (brname.find("HLT_") == std::string::npos and brname.find("L1_") == std::string::npos)
                cout << brname << ", ";
            _originalvars.push_back(abranch->GetName());
        }
    }
    cout << endl;
}

NanoAODAnalyzerrdframe::~NanoAODAnalyzerrdframe() {

    // TODO Auto-generated destructor stub
    // ugly...
    std::cout<<">>  Job Done  <<"<<std::endl;
}

bool NanoAODAnalyzerrdframe::isDefined(string v) {

	auto result = std::find(_originalvars.begin(), _originalvars.end(), v);
	if (result != _originalvars.end()) return true;
	else return false;
}

void NanoAODAnalyzerrdframe::setTree(TTree *t, std::string outfilename) {

	_rd = ROOT::RDataFrame(*t);
	_rlm = RNode(_rd);
	_outfilename = outfilename;
	_hist1dinfovector.clear();
	_th1dhistos.clear();
	_varstostore.clear();
	_hist1dinfovector.clear();
	_selections.clear();

	this->setupAnalysis();
}

void NanoAODAnalyzerrdframe::setupAnalysis() {

    if (_isData) _jsonOK = readjson();

    //_rlm = _rlm.Filter("event < 12534199");

    // Event weight for data it's always one. For MC, it depends on the sign
    _rlm = _rlm.Define("one", "1.0");
    if(_isSkim){
        if(_isData){
            _rlm = _rlm.Define("unitGenWeight","one")
                       .Define("puWeight","one")
                       .Define("muonWeightId","one")
                       .Define("muonWeightIso","one")
                       .Define("muonWeightTrg","one")
                       .Define("btagWeight_DeepFlavB","one")
                       .Define("btagWeight_DeepFlavB_jes","one");
        } else {
            // pu weight setup
            cout<<"Loading Pileup profiles"<<endl;
            // MC 2016pre = MC 2016post (same file)
            TFile tfmc(("data/Pileup/PileupMC_UL" + _year + ".root").c_str());
            _hpumc = dynamic_cast<TH1D *>(tfmc.Get("pu_mc"));
            _hpumc->SetDirectory(0);
            tfmc.Close();

            TFile tfdata(("data/Pileup/PileupDATA_UL" + _year + ".root").c_str());
            _hpudata = dynamic_cast<TH1D *>(tfdata.Get("pileup"));
            _hpudata_plus = dynamic_cast<TH1D *>(tfdata.Get("pileup_plus"));
            _hpudata_minus = dynamic_cast<TH1D *>(tfdata.Get("pileup_minus"));

            _hpudata->SetDirectory(0);
            _hpudata_plus->SetDirectory(0);
            _hpudata_minus->SetDirectory(0);
            tfdata.Close();

            _puweightcalc = new WeightCalculatorFromHistogram(_hpumc, _hpudata);
            _puweightcalc_plus = new WeightCalculatorFromHistogram(_hpumc, _hpudata_plus);
            _puweightcalc_minus = new WeightCalculatorFromHistogram(_hpumc, _hpudata_minus);

            _rlm = _rlm.Define("unitGenWeight","genWeight != 0 ? genWeight/abs(genWeight) : 0")
                       .Define("puWeight", [this](float x) ->std::vector<float>
                              {return {_puweightcalc->getWeight(x), _puweightcalc_plus->getWeight(x), _puweightcalc_minus->getWeight(x)};}, {"Pileup_nTrueInt"});
        }
    }

    std::vector<std::string> jes_var;
    if (_isRun16)
        jes_var = jes_var_2016;
    else if (_isRun17)
        jes_var = jes_var_2017;
    else if (_isRun18)
        jes_var = jes_var_2018;
    else
        cout << "WARNING !!!!!! : No JES - BTAG SF found" << endl;

    // Object selection will be defined in sequence.
    // Selected objects will be stored in new vectors.
    if (_isSkim) {
        selectMuons();
        setupJetMETCorrection(_globaltag, jes_var, "AK4PFchs", _isData);
        skimJets();
        if (!_isData){
            calculateEvWeight();
            applyBSFs(jes_var);
        }
    } else {
        selectElectrons();
        selectMuons();
        selectJets();
        selectTaus();
        removeOverlaps();
    }
    defineMoreVars();
    defineCuts();
    bookHists();
    setupCuts_and_Hists();
    setupTree();
}

bool NanoAODAnalyzerrdframe::readjson() {

	auto isgoodjsonevent = [this](unsigned int runnumber, unsigned int lumisection) {

			auto key = std::to_string(runnumber);

			bool goodeventflag = false;

			if (jsonroot.isMember(key)) {
				Json::Value runlumiblocks = jsonroot[key];
				for (unsigned int i=0; i<runlumiblocks.size() && !goodeventflag; i++) {
					auto lumirange = runlumiblocks[i];
					if (lumisection >= lumirange[0].asUInt() && lumisection <= lumirange[1].asUInt()) goodeventflag = true;
				}
				return goodeventflag;
			} else {
				//cout << "Run not in json " << runnumber << endl;
				return false;
			}

		};

	if (_jsonfname != "") {
		std::ifstream jsoninfile;
		jsoninfile.open(_jsonfname);

		if (jsoninfile.good()) {
			jsoninfile >> jsonroot;
			/*
			auto runlumiblocks =  jsonroot["276775"];
			for (auto i=0; i<runlumiblocks.size(); i++)
			{
				auto lumirange = runlumiblocks[i];
				cout << "lumi range " << lumirange[0] << " " << lumirange[1] << endl;
			}
			*/
			_rlm = _rlm.Define("goodjsonevent", isgoodjsonevent, {"run", "luminosityBlock"}).Filter("goodjsonevent");
			_jsonOK = true;
			return true;
		} else {
			cout << "Problem reading json file " << _jsonfname << endl;
			return false;
		}
	} else {
		cout << "no JSON file given" << endl;
		return true;
	}
}

void NanoAODAnalyzerrdframe::selectElectrons() {

    //cout << "select electrons" << endl;
    // Run II recommendation: https://twiki.cern.ch/twiki/bin/viewauth/CMS/EgammaRunIIRecommendations
    // Run II recomendation - cutbased: https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedElectronIdentificationRun2
    // Temporary elecuts (Not to be used!)
    //_rlm = _rlm.Define("elecuts", "Electron_pt>15.0 && abs(Electron_eta)<2.4 && Electron_cutBased == 1 && ((abs(Electron_deltaEtaSC<=1.479) && abs(Electron_dxy) < 0.05 && abs(Electron_dz) < 0.10 ) || (abs(Electron_deltaEtaSC>1.479) && abs(Electron_dxy) < 0.10 && abs(Electron_dz) < 0.20))")
    //           .Define("Sel_elept", "Electron_pt[elecuts]") // define new variables
    //           .Define("Sel_eleta", "Electron_eta[elecuts]")
    //           .Define("Sel_elephi", "Electron_phi[elecuts]")
    //           .Define("Sel_elemass", "Electron_mass[elecuts]")
    //           .Define("Sel_eleidx", ::good_idx, {"elecuts"})
    //           .Define("nelepass", "int(Sel_elept.size())")
    //           .Define("ele4vecs", ::gen4vec, {"Sel_elept", "Sel_eleta", "Sel_elephi", "Sel_elemass"});

    _rlm = _rlm.Define("vetoelecuts", "Electron_pt>15.0 && abs(Electron_eta)<2.4 && Electron_cutBased == 1")
               .Define("nvetoelepass","Sum(vetoelecuts)");
}

void NanoAODAnalyzerrdframe::selectMuons() {

    _rlm = _rlm.Define("muoncuts", "Muon_pt>50.0 && abs(Muon_eta)<2.4 && Muon_tightId && Muon_pfRelIso04_all<0.15");
    //cout << "select muons" << endl;
    _rlm = _rlm.Redefine("Muon_pt", "Muon_pt[muoncuts]")
               .Redefine("Muon_eta", "Muon_eta[muoncuts]")
               .Redefine("Muon_phi", "Muon_phi[muoncuts]")
               .Redefine("Muon_mass", "Muon_mass[muoncuts]")
               .Redefine("Muon_charge", "Muon_charge[muoncuts]")
               .Define("Sel_muonidx", ::good_idx, {"muoncuts"})
               .Define("nmuonpass", "int(Muon_pt.size())")
               .Define("muon4vecs", ::gen4vec, {"Muon_pt", "Muon_eta", "Muon_phi", "Muon_mass"});

    _rlm = _rlm.Define("vetomuoncuts", "!muoncuts && Muon_pt>15.0 && abs(Muon_eta)<2.4 && Muon_looseId && Muon_pfRelIso04_all<0.25")
               .Define("nvetomuons","Sum(vetomuoncuts)");
}

/*
void NanoAODAnalyzerrdframe::selectMET()
{
    _rlm = _rlm.Define("met4vec", ::genmet4vec, {"MET_pt","MET_phi"});
}*/

void NanoAODAnalyzerrdframe::setupJetMETCorrection(string globaltag, std::vector<std::string> jes_var, std::string jetalgo, bool dataMc) {

    std::vector<JetCorrectionUncertainty*> regroupedUnc;
    if (_globaltag != "") {
        cout << "Applying new JetMET corrections. GT: " + _globaltag + " on jetAlgo: AK4PFchs" << endl;
        string basedirectory = "data/jme/";

        string datamcflag = "";
        if (dataMc) datamcflag = "DATA";
        else datamcflag = "MC";

        // set file names that contain the parameters for corrections
        string dbfilenamel1 = basedirectory + _globaltag + "_" + datamcflag + "_L1FastJet_" + jetalgo + ".txt";
        string dbfilenamel2 = basedirectory + _globaltag + "_" + datamcflag + "_L2Relative_" + jetalgo + ".txt";
        string dbfilenamel3 = basedirectory + _globaltag + "_" + datamcflag + "_L3Absolute_" + jetalgo + ".txt";
        string dbfilenamel2l3 = basedirectory + _globaltag + "_" + datamcflag + "_L2L3Residual_" + jetalgo + ".txt";

        JetCorrectorParameters *L1JetCorrPar = new JetCorrectorParameters(dbfilenamel1);
        if (!L1JetCorrPar->isValid()) {
          std::cerr << "L1FastJet correction parameters not read" << std::endl;
          exit(1);
        }

        JetCorrectorParameters *L2JetCorrPar = new JetCorrectorParameters(dbfilenamel2);
        if (!L2JetCorrPar->isValid()) {
            std::cerr << "L2Relative correction parameters not read" << std::endl;
            exit(1);
        }

        JetCorrectorParameters *L3JetCorrPar = new JetCorrectorParameters(dbfilenamel3);
        if (!L3JetCorrPar->isValid()) {
            std::cerr << "L3Absolute correction parameters not read" << std::endl;
            exit(1);
        }

        JetCorrectorParameters *L2L3JetCorrPar = new JetCorrectorParameters(dbfilenamel2l3);
        if (!L2L3JetCorrPar->isValid()) {
            std::cerr << "L2L3Residual correction parameters not read" << std::endl;
            exit(1);
        }

        // to apply all the corrections, first collect them into a vector
        std::vector<JetCorrectorParameters> jetc;
        jetc.push_back(*L1JetCorrPar);
        jetc.push_back(*L2JetCorrPar);
        jetc.push_back(*L3JetCorrPar);
        jetc.push_back(*L2L3JetCorrPar);

        // apply the various corrections
        _jetCorrector = new FactorizedJetCorrector(jetc);

        // object to calculate uncertainty
        cout<<"Applying JEC Uncertainty"<<endl;
        for (std::string src : jes_var) {
            if (src.find("up") != std::string::npos) {
                auto uncsource = src.substr(3, src.size()-2-3);
                cout << "JEC Uncertainty Source : " + uncsource << endl;
                string dbfilenameunc = basedirectory + "RegroupedV2_" + _globaltag + "_MC_UncertaintySources_AK4PFchs.txt";
                JetCorrectorParameters *uncCorrPar = new JetCorrectorParameters(dbfilenameunc, uncsource);
                _jetCorrectionUncertainty = new JetCorrectionUncertainty(*uncCorrPar);
                regroupedUnc.emplace_back(_jetCorrectionUncertainty);
            } else {
                continue; //We only need var name, no up/down
            }
        }
    }

    auto applyJes = [this](floats jetpts, floats jetetas, floats jetAreas, floats jetrawf, float rho, floats tocorrect)->floats {

        floats corrfactors;
        corrfactors.reserve(jetpts.size());

        for (unsigned int i =0; i<jetpts.size(); i++) {
            float rawfrac = 1.0-jetrawf[i];
            float rawjetpt = jetpts[i] * (rawfrac);
            _jetCorrector->setJetPt(rawjetpt);
            _jetCorrector->setJetEta(jetetas[i]);
            _jetCorrector->setJetA(jetAreas[i]);
            _jetCorrector->setRho(rho);
            float corrfactor = _jetCorrector->getCorrection();
            corrfactors.emplace_back(tocorrect[i] * rawfrac * corrfactor);
        }
        return corrfactors;
    };

    // structure: jes[jetIdx][varIdx]
    auto jesUnc = [this, regroupedUnc](floats jetpts, floats jetetas, floats jetAreas, floats jetrawf, float rho)->std::vector<std::vector<float>> {

        std::vector<float> uncSources;
        uncSources.reserve(2 * regroupedUnc.size());
        std::vector<std::vector<float>> uncertainties;
        uncertainties.reserve(jetpts.size());

        for (unsigned int i =0; i<jetpts.size(); i++) {
            for (size_t j=0; j<regroupedUnc.size(); j++) {
                auto corrector = regroupedUnc[j];

                corrector->setJetPt(jetpts[i]);
                corrector->setJetEta(jetetas[i]);
                float unc = corrector->getUncertainty(true);
                uncSources.emplace_back(1.0f + unc);
                uncSources.emplace_back(1.0f - unc);
            }
            uncertainties.emplace_back(uncSources);
            uncSources.clear();
        }
        return uncertainties;
    };

    auto metCorr = [](float met, float metphi, floats jetptsbefore, floats jetptsafter, floats jetphis)->float {

        auto metx = met * cos(metphi);
        auto mety = met * sin(metphi);

        for (unsigned int i=0; i<jetphis.size(); i++) {
            if (jetptsafter[i] > 15.0) {
                metx -= (jetptsafter[i] - jetptsbefore[i])*cos(jetphis[i]);
                mety -= (jetptsafter[i] - jetptsbefore[i])*sin(jetphis[i]);
            }
        }
        return (float(sqrt(metx*metx + mety*mety)));
    };

    auto metUnc = [](float met, float metphi, floats jetptsbefore, std::vector<std::vector<float>> jetptscorr, floats jetphis)->floats {

        floats corrfactors;
        corrfactors.reserve(static_cast<int>(jetptscorr.size()));

        for (size_t j=0; j<jetptscorr[0].size(); j++) {
            auto metx = met * cos(metphi);
            auto mety = met * sin(metphi);

            for (unsigned int i=0; i<jetphis.size(); i++) {
                if (jetptsbefore[i] * jetptscorr[i][j] > 15.0) {
                    metx -= (jetptscorr[i][j] - 1.0) * jetptsbefore[i] * cos(jetphis[i]);
                    mety -= (jetptscorr[i][j] - 1.0) * jetptsbefore[i] * sin(jetphis[i]);
                }
            }
            corrfactors.emplace_back(float(sqrt(metx*metx + mety*mety)));
        }
        return corrfactors;
    };

    auto metPhiCorr = [](float met, float metphi, floats jetptsbefore, floats jetptsafter, floats jetphis)->float {

        auto metx = met * cos(metphi);
        auto mety = met * sin(metphi);

        for (unsigned int i=0; i<jetphis.size(); i++) {
            if (jetptsafter[i] > 15.0) {
                metx -= (jetptsafter[i] - jetptsbefore[i])*cos(jetphis[i]);
                mety -= (jetptsafter[i] - jetptsbefore[i])*sin(jetphis[i]);
            }
        }
        return float(atan2(mety, metx));
    };

    auto metPhiUnc = [](float met, float metphi, floats jetptsbefore, std::vector<std::vector<float>> jetptscorr, floats jetphis)->floats {

        floats corrfactors;
        corrfactors.reserve(static_cast<int>(jetptscorr.size()));

        for (size_t j=0; j<jetptscorr[0].size(); j++) {
            auto metx = met * cos(metphi);
            auto mety = met * sin(metphi);

            for (unsigned int i=0; i<jetphis.size(); i++) {
                if (jetptsbefore[i] * jetptscorr[i][j] > 15.0) {
                    metx -= (jetptscorr[i][j] - 1.0) * jetptsbefore[i] * cos(jetphis[i]);
                    mety -= (jetptscorr[i][j] - 1.0) * jetptsbefore[i] * sin(jetphis[i]);
                }
            }
            corrfactors.emplace_back(float(atan2(mety, metx)));
        }
        return corrfactors;
    };

    //FIXME: should correct jet mass. but can we do it at once?
    if (_jetCorrector != 0) {
        _rlm = _rlm.Redefine("Jet_pt_uncorr", "Jet_pt");
        _rlm = _rlm.Define("Jet_pt_corr", applyJes, {"Jet_pt", "Jet_eta", "Jet_area", "Jet_rawFactor", "fixedGridRhoFastjetAll", "Jet_pt"})
                   .Redefine("Jet_mass", applyJes, {"Jet_pt", "Jet_eta", "Jet_area", "Jet_rawFactor", "fixedGridRhoFastjetAll", "Jet_mass"})
                   .Redefine("MET_pt", metCorr, {"MET_pt", "MET_phi", "Jet_pt", "Jet_pt_corr", "Jet_phi"})
                   .Redefine("MET_phi", metPhiCorr, {"MET_pt", "MET_phi", "Jet_pt", "Jet_pt_corr", "Jet_phi"});
        if (!dataMc) {
            _rlm = _rlm.Define("Jet_pt_unc", jesUnc, {"Jet_pt", "Jet_eta", "Jet_area", "Jet_rawFactor", "fixedGridRhoFastjetAll"})
                       .Define("MET_pt_unc", metUnc, {"MET_pt", "MET_phi", "Jet_pt", "Jet_pt_unc", "Jet_phi"})
                       .Define("MET_phi_unc", metPhiUnc, {"MET_pt", "MET_phi", "Jet_pt", "Jet_pt_unc", "Jet_phi"});
        }
        _rlm = _rlm.Redefine("Jet_pt", "Jet_pt_corr");
    }
}

void NanoAODAnalyzerrdframe::skimJets() {

    float jetPtCut = 30;
    float jetEtaCut = 2.4;
    int jetIdCut = 6;

    // input vector: vec[pt][vars]
    // vec<vec<float>> or similar form were not able to be skimmed!?
    // Note: do not skim with exact value of pt!
    auto skimJetCol = [this, jetPtCut, jetEtaCut, jetIdCut](std::vector<std::vector<float>> toSkim, floats pts, floats etas, ints ids)->std::vector<std::vector<float>> {

        std::vector<float> newvars;
        newvars.reserve(toSkim[0].size());
        std::vector<std::vector<float>> out;

        for (size_t i =0; i<toSkim.size(); i++) {
            if (pts[i] < jetPtCut) continue;
            if (ids[i] != jetIdCut) continue;
            if (abs(etas[i]) > jetEtaCut) continue;

            for (size_t j=0; j<toSkim[0].size(); j++) {
                newvars.emplace_back(toSkim[i][j]);
            }
            out.emplace_back(newvars);
            newvars.clear();
        }
        return out;
    };

    // skim jet collection
    _rlm = _rlm.Define("jetcuts", "Jet_pt>30.0 && abs(Jet_eta)<2.4 && Jet_jetId == 6")
               .Define("Jet_pt_unc2", skimJetCol, {"Jet_pt_unc", "Jet_pt", "Jet_eta", "Jet_jetId"});
    _rlm = _rlm.Redefine("Jet_pt", "Jet_pt[jetcuts]")
               .Redefine("Jet_eta", "Jet_eta[jetcuts]")
               .Redefine("Jet_phi", "Jet_phi[jetcuts]")
               .Redefine("Jet_jetId", "Jet_jetId[jetcuts]")
               .Redefine("Jet_hadronFlavour","Jet_hadronFlavour[jetcuts]");

}

void NanoAODAnalyzerrdframe::applyBSFs(std::vector<string> jes_var) {

    cout << "Loading Btag SF" << endl;
    string btagpath = "data/btagSF/";

    BTagCalibration _btagcalib = {"DeepJet", btagpath + "skimmed_btag_" + _year + ".csv"};
    cout << "    Loaded file : " << btagpath + "skimmed_btag_" + _year + ".csv" << endl;
    BTagCalibration _btagcalibJes = {"DeepJet", btagpath + "skimmed_jes_" + _year + ".csv"};
    cout << "    Loaded file : " << btagpath + "skimmed_jes_" + _year + ".csv" << endl;

    _rlm = _rlm.Define("btag_var", [](){return strings(btag_var);})
               .Define("btag_jes_var", [jes_var](){return strings(jes_var);});


    BTagCalibrationReader _btagcalibreader = {BTagEntry::OP_RESHAPING, "central", btag_var};
    BTagCalibrationReader _btagcalibreaderJes = {BTagEntry::OP_RESHAPING, "central", jes_var};

    // load the formulae b flavor tagging
    _btagcalibreader.load(_btagcalib, BTagEntry::FLAV_B, "iterativefit");
    _btagcalibreader.load(_btagcalib, BTagEntry::FLAV_C, "iterativefit");
    _btagcalibreader.load(_btagcalib, BTagEntry::FLAV_UDSG, "iterativefit");
    _btagcalibreaderJes.load(_btagcalibJes, BTagEntry::FLAV_B, "iterativefit");
    _btagcalibreaderJes.load(_btagcalibJes, BTagEntry::FLAV_C, "iterativefit");
    _btagcalibreaderJes.load(_btagcalibJes, BTagEntry::FLAV_UDSG, "iterativefit");

    // function to calculate event weight for MC events based on DeepJet algorithm
    auto btagweightgenerator = [this, _btagcalibreader](floats &pts, floats &etas, ints &hadflav, floats &btags, strings &var)->doubles {

        doubles bSFs;
        for (std::string src : var) {
            double bweight = 1.0;
            for (unsigned int i=0; i<pts.size(); i++) {
                if (pts[i] < 40) continue;
                if (src.find("cferr") != std::string::npos and hadflav[i] != 4) continue;
                if (src.find("cferr") == std::string::npos and hadflav[i] == 4) continue;

                BTagEntry::JetFlavor hadfconv;
                if      (hadflav[i]==5) hadfconv=BTagEntry::FLAV_B;
                else if (hadflav[i]==4) hadfconv=BTagEntry::FLAV_C;
                else                    hadfconv=BTagEntry::FLAV_UDSG;
                double w = _btagcalibreader.eval_auto_bounds(src, hadfconv, fabs(etas[i]), pts[i], btags[i]);
                bweight *= w;
            }
            bSFs.emplace_back(bweight);
        }
        return bSFs;
    };

    auto btagweightgeneratorJes = [this, _btagcalibreaderJes](floats &pts, floats &etas, ints &hadflav, floats &btags, std::vector<std::vector<float>> jes, strings &var)->doubles {

       doubles bSFs;
        for (size_t i=0; i<var.size(); i++) {
            double bweight = 1.0;
            std::string src = var[i];

            for (unsigned int j=0; j<pts.size(); j++) {
                auto newpt = pts[j] * jes[j][i];
                if (newpt < 40) continue;

                BTagEntry::JetFlavor hadfconv;
                if      (hadflav[j]==5) hadfconv=BTagEntry::FLAV_B;
                else if (hadflav[j]==4) hadfconv=BTagEntry::FLAV_C;
                else                    hadfconv=BTagEntry::FLAV_UDSG;
                double w = _btagcalibreaderJes.eval_auto_bounds(src, hadfconv, fabs(etas[j]), newpt, btags[j]);
                bweight *= w;
            }
            bSFs.emplace_back(bweight);
        }
        return bSFs;
    };

    cout << "Generate b-tagging weight" << endl;
    _rlm = _rlm.Define("btagWeight_DeepFlavB", btagweightgenerator, {"Jet_pt", "Jet_eta", "Jet_hadronFlavour", "Jet_btagDeepFlavB", "btag_var"})
               .Define("btagWeight_DeepFlavB_jes", btagweightgeneratorJes, {"Jet_pt", "Jet_eta", "Jet_hadronFlavour", "Jet_btagDeepFlavB", "Jet_pt_unc", "btag_jes_var"});
}

void NanoAODAnalyzerrdframe::selectJets()
{
	// apparently size() returns long int, which ROOT doesn't recognized for branch types
	// , so it must be cast into int if you want to save them later into a TTree
        if (_globaltag != "") {
            if (_isSystJes) {
                if (_isSystUp) {
                    _rlm = _rlm.Define("Sys_jetpt","Jet_pt_up");
                    _rlm = _rlm.Define("Sys_METpt","MET_pt_up");
                    _rlm = _rlm.Define("Sys_METphi","MET_phi_up");
                } else if (_isSystDown) {
                    _rlm = _rlm.Define("Sys_jetpt","Jet_pt_down");
                    _rlm = _rlm.Define("Sys_METpt","MET_pt_down");
                    _rlm = _rlm.Define("Sys_METphi","MET_phi_down");
                }
            }
        }
        _rlm = _rlm.Define("jetcuts", "Jet_pt>40.0 && abs(Jet_eta)<2.4 && Jet_jetId == 6");
        _rlm = _rlm.Redefine("Jet_pt", "Jet_pt[jetcuts]")
                   .Redefine("Jet_eta", "Jet_eta[jetcuts]")
                   .Redefine("Jet_phi", "Jet_phi[jetcuts]")
                   .Redefine("Jet_mass", "Jet_mass[jetcuts]")
                   .Redefine("Jet_btagDeepFlavB", "Jet_btagDeepFlavB[jetcuts]")
                   .Redefine("nJet", "int(Jet_pt.size())")
                   .Define("jet4vecs", ::gen4vec, {"Jet_pt", "Jet_eta", "Jet_phi", "Jet_mass"});
}

void NanoAODAnalyzerrdframe::selectTaus()
{
        auto overlap_removal_mutau = [](FourVectorVec &muon4vecs, FourVectorVec &tau4vecs){
                ints out;
                for (auto tau: tau4vecs){
                        int check = 0;
                        for (auto mu: muon4vecs){
                                auto dR = ROOT::Math::VectorUtil::DeltaR(mu, tau);
                                if( dR >= 0.4 ) check = 1;
                        }
                        out.emplace_back(check);
                }
                return out;
        };
        _rlm = _rlm.Define("tau4vecs", ::gen4vec, {"Scaled_taupt", "Tau_eta", "Tau_phi", "Scaled_taumass"})
                   .Define("mutauoverlap", overlap_removal_mutau, {"muon4vecs","tau4vecs"});

        // Hadronic Tau Object Selections
        _rlm = _rlm.Define("taucuts", "Scaled_taupt>40.0 && abs(Tau_eta)<2.3 && Tau_idDecayModeNewDMs")
                   .Define("deeptauidcuts","Tau_idDeepTau2017v2p1VSmu & 8 && Tau_idDeepTau2017v2p1VSe & 4 && Tau_idDeepTau2017v2p1VSjet & 64");

        // Hadronic Tau Selection
        _rlm = _rlm.Define("seltaucuts","taucuts && deeptauidcuts && mutauoverlap")
                   .Define("Sel_taupt", "Scaled_taupt[seltaucuts]")
                   .Define("Sel_taueta", "Tau_eta[seltaucuts]")
                   .Define("Sel_tauphi", "Tau_phi[seltaucuts]")
                   .Define("Sel_taumass", "Scaled_taumass[seltaucuts]")
                   .Define("Sel_taucharge", "Tau_charge[seltaucuts]")
                   .Define("Sel_taujetidx", "Tau_jetIdx[seltaucuts]")
                   .Define("Sel_tauflav","Tau_genPartFlav[seltaucuts]")
                   .Define("ncleantaupass", "int(Sel_taupt.size())")
                   .Define("cleantau4vecs", ::gen4vec, {"Sel_taupt", "Sel_taueta", "Sel_tauphi", "Sel_taumass"});

}

void NanoAODAnalyzerrdframe::removeOverlaps()
{
	// for checking overlapped jets with leptons
        auto checkoverlap = [](FourVectorVec &seljets, FourVectorVec &sellep)
        {
                doubles mindrlepton;
                for (auto ajet: seljets)
                {
                        auto mindr = 6.0;
                        for ( auto alepton : sellep )
                        {
                                auto dr = ROOT::Math::VectorUtil::DeltaR(ajet, alepton);
                                if (dr < mindr) mindr = dr;
                        }
                        int out = mindr >= 0.4 ? 1 : 0;
                        mindrlepton.emplace_back(out);
                }
                return mindrlepton;
        };

	// Overlap removal with muon (used for btagging SF)
        _rlm = _rlm.Define("muonjetoverlap", checkoverlap, {"jet4vecs","muon4vecs"})
                   .Define("taujetoverlap", checkoverlap, {"jet4vecs","cleantau4vecs"})
                   .Define("jetoverlap","muonjetoverlap && taujetoverlap");

        _rlm = _rlm.Define("Sel2_jetpt", "Sel_jetpt[jetoverlap]")
                   .Define("Sel2_jeteta", "Sel_jeteta[jetoverlap]")
                   .Define("Sel2_jetphi", "Sel_jetphi[jetoverlap]")
                   .Define("Sel2_jetmass", "Sel_jetmass[jetoverlap]")
                   .Define("Sel2_jetbtag", "Sel_jetbtag[jetoverlap]")
                   .Define("ncleanjetspass", "int(Sel2_jetpt.size())")
                   .Define("cleanjet4vecs", ::gen4vec, {"Sel2_jetpt", "Sel2_jeteta", "Sel2_jetphi", "Sel2_jetmass"})
                   .Define("Sel2_jetHT", "Sum(Sel2_jetpt)");

        if(_isRun16pre){
                //https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL16preVFP
                _rlm = _rlm.Define("btagcuts", "Sel2_jetbtag>0.2598"); //l: 0.0508, m: 0.2598, t: 0.6502
        }else if(_isRun16post){
                //https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL16postVFP#AK4_b_tagging
                _rlm = _rlm.Define("btagcuts", "Sel2_jetbtag>0.2489"); //l: 0.0480, m: 0.2489, t: 0.6377
        }else if(_isRun17){
                //https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation106XUL17
                _rlm = _rlm.Define("btagcuts", "Sel2_jetbtag>0.3040"); //l: 0.0532, m: 0.3040, t: 0.7476
        }else if(_isRun18){
                //https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation106XUL18
                _rlm = _rlm.Define("btagcuts", "Sel2_jetbtag>0.2783"); //l: 0.0490, m: 0.2783, t: 0.7100
        }

        _rlm = _rlm.Define("Sel2_bjetpt", "Sel2_jetpt[btagcuts]")
                   .Define("Sel2_bjeteta", "Sel2_jeteta[btagcuts]")
                   .Define("Sel2_bjetphi", "Sel2_jetphi[btagcuts]")
                   .Define("Sel2_bjetmass", "Sel2_jetmass[btagcuts]")
                   .Define("Sel2_bjetbtag", "Sel2_jetbtag[btagcuts]")
                   .Define("ncleanbjetspass", "int(Sel2_bjetpt.size())")
                   .Define("Sel2_bjetHT", "Sum(Sel2_bjetpt)")
                   .Define("cleanbjet4vecs", ::gen4vec, {"Sel2_bjetpt", "Sel2_bjeteta", "Sel2_bjetphi", "Sel2_bjetmass"});

}

void NanoAODAnalyzerrdframe::matchGenReco()
{
        _rlm = _rlm.Define("FinalGenPart_idx", ::FinalGenPart_idx, {"GenPart_pdgId", "GenPart_genPartIdxMother"})
                   .Define("GenPart_LFVup_idx", "FinalGenPart_idx[0]")
                   .Define("GenPart_LFVmuon_idx", "FinalGenPart_idx[1]")
                   .Define("GenPart_LFVtau_idx", "FinalGenPart_idx[2]")
                   .Define("GenPart_SMb_idx", "FinalGenPart_idx[3]")
                   .Define("GenPart_SMW1_idx", "FinalGenPart_idx[4]")
                   .Define("GenPart_SMW2_idx", "FinalGenPart_idx[5]")
                   .Define("GenPart_LFVtop_idx", "FinalGenPart_idx[6]")
                   .Define("GenPart_SMtop_idx", "FinalGenPart_idx[7]");

        _rlm = _rlm.Define("drmax1", "float(0.15)")
                   .Define("drmax2", "float(0.4)")
                   .Define("Muon_matched", ::dRmatching_binary,{"GenPart_LFVmuon_idx","drmax1","GenPart_pt","GenPart_eta","GenPart_phi","GenPart_mass","Muon_pt","Muon_eta","Muon_phi","Muon_mass"})
                   .Define("Tau_matched",::dRmatching_binary,{"GenPart_LFVtau_idx","drmax2", "GenPart_pt","GenPart_eta","GenPart_phi","GenPart_mass","Tau_pt","Tau_eta","Tau_phi","Tau_mass"})
                   .Define("Jet_LFVup_matched",::dRmatching_binary,{"GenPart_LFVup_idx","drmax2","GenPart_pt","GenPart_eta","GenPart_phi","GenPart_mass","Jet_pt","Jet_eta","Jet_phi","Jet_mass"})
                   .Define("Jet_SMb_matched",::dRmatching_binary,{"GenPart_SMb_idx","drmax2","GenPart_pt","GenPart_eta","GenPart_phi","GenPart_mass","Jet_pt","Jet_eta","Jet_phi","Jet_mass"})
                   .Define("Jet_SMW1_matched",::dRmatching_binary,{"GenPart_SMW1_idx","drmax2","GenPart_pt","GenPart_eta","GenPart_phi","GenPart_mass","Jet_pt","Jet_eta","Jet_phi","Jet_mass"})
                   .Define("Jet_SMW2_matched",::dRmatching_binary,{"GenPart_SMW2_idx","drmax2", "GenPart_pt","GenPart_eta","GenPart_phi","GenPart_mass","Jet_pt","Jet_eta","Jet_phi","Jet_mass"})
                   .Define("Sel_muon_matched","Muon_matched[muoncuts]")
                   .Define("Sel_tau_matched","Tau_matched[seltaucuts]")
                   .Define("Sel2_LFVupjet_matched","Jet_LFVup_matched[jetcuts][muonjetoverlap][taujetoverlap]")
                   .Define("Sel2_SMbjet_matched","Jet_SMb_matched[jetcuts][muonjetoverlap][taujetoverlap]")
                   .Define("Sel2_SMW1jet_matched","Jet_SMW1_matched[jetcuts][muonjetoverlap][taujetoverlap]")
                   .Define("Sel2_SMW2jet_matched","Jet_SMW2_matched[jetcuts][muonjetoverlap][taujetoverlap]")
                   .Define("Sel_muonmatched_idx","ArgMax(Sel_muon_matched)")
                   .Define("Sel_taumatched_idx","ArgMax(Sel_tau_matched)")
                   .Define("Sel2_LFVupjet_matched_idx","ArgMax(Sel2_LFVupjet_matched)")
                   .Define("Sel2_SMbjet_matched_idx","ArgMax(Sel2_SMbjet_matched)")
                   .Define("Sel2_SMW1jet_matched_idx","ArgMax(Sel2_SMW1jet_matched)")
                   .Define("Sel2_SMW2jet_matched_idx","ArgMax(Sel2_SMW2jet_matched)")
                   .Define("nmuonmatched", "Sum(Muon_matched)")
                   .Define("ntaumatched", "Sum(Tau_matched)")
                   .Define("nJet_LFVup_matched", "Sum(Jet_LFVup_matched)")
                   .Define("nJet_SMb_matched", "Sum(Jet_SMb_matched)")
                   .Define("nJet_SMW1_matched", "Sum(Jet_SMW1_matched)")
                   .Define("nJet_SMW2_matched", "Sum(Jet_SMW2_matched)");
}

void NanoAODAnalyzerrdframe::selectFatJets()
{
	_rlm = _rlm.Define("fatjetcuts", "FatJet_pt>400.0 && abs(FatJet_eta)<2.4 && FatJet_tau1>0.0 && FatJet_tau2>0.0 && FatJet_tau3>0.0 && FatJet_tau3/FatJet_tau2<0.5")
				.Define("Sel_fatjetpt", "FatJet_pt[fatjetcuts]")
				.Define("Sel_fatjeteta", "FatJet_eta[fatjetcuts]")
				.Define("Sel_fatjetphi", "FatJet_phi[fatjetcuts]")
				.Define("Sel_fatjetmass", "FatJet_mass[fatjetcuts]")
				.Define("nfatjetspass", "int(Sel_fatjetpt.size())")
				//.Define("Sel_fatjetweight", "std::vector<double>(nfatjetspass, evWeight)")
				.Define("Sel_fatjet4vecs", ::gen4vec, {"Sel_fatjetpt", "Sel_fatjeteta", "Sel_fatjetphi", "Sel_fatjetmass"});
}

void NanoAODAnalyzerrdframe::calculateEvWeight() {

    // Muon SF
    cout<<"Loading Muon SF"<<endl;
    std::string muonFile = _year + "_UL";
    std::string muonTrgHist = "";
    TFile *muontrg;
    TFile *muonid;
    TFile *muoniso;

    if (_isRun16pre) {
        muonFile = "2016_UL_HIPM_";
        muonTrgHist = "NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt";
    } else if (_isRun16post) {
        muonFile = "2016_UL_";
        muonTrgHist = "NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt";
    } else if (_isRun17) {
        muonTrgHist = "NUM_IsoMu27_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt";
    } else if (_isRun18) {
        muonTrgHist = "NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt";
    }
    muonid = TFile::Open(("data/MuonSF/Efficiencies_muon_generalTracks_Z_Run" + muonFile + "_ID.root").c_str());
    TH2F* _hmuonid = dynamic_cast<TH2F *>(muonid->Get("NUM_TightID_DEN_TrackerMuons_abseta_pt"));
    _hmuonid->SetDirectory(0);
    muonid->Close();
    WeightCalculatorFromHistogram* _muonid = new WeightCalculatorFromHistogram(_hmuonid);

    muoniso = TFile::Open(("data/MuonSF/Efficiencies_muon_generalTracks_Z_Run" + muonFile + "_ISO.root").c_str());
    TH2F* _hmuoniso = dynamic_cast<TH2F *>(muoniso->Get("NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt"));
    _hmuoniso->SetDirectory(0);
    muoniso->Close();
    WeightCalculatorFromHistogram* _muoniso = new WeightCalculatorFromHistogram(_hmuoniso);

    muontrg = TFile::Open(("data/MuonSF/Efficiencies_muon_generalTracks_Z_Run" + muonFile + "_SingleMuonTriggers.root").c_str());
    TH2F* _hmuontrg = dynamic_cast<TH2F *>(muontrg->Get(muonTrgHist.c_str()));
    _hmuontrg->SetDirectory(0);
    muontrg->Close();
    WeightCalculatorFromHistogram* _muontrg = new WeightCalculatorFromHistogram(_hmuontrg);

    auto muonSFId = [this, _muonid](floats &pt, floats &eta)->std::vector<float> {
        std::vector<float> wVec;
        if (pt.size() > 0) {
            for (unsigned int i=0; i<pt.size(); i++)
                wVec.emplace_back(_muonid->getWeight(std::abs(eta[i]),pt[i]));
        }
        return wVec;
    };

    auto muonSFIso = [this, _muoniso](floats &pt, floats &eta)->std::vector<float> {
        std::vector<float> wVec;
        if (pt.size() > 0) {
            for (unsigned int i=0; i<pt.size(); i++)
                wVec.emplace_back(_muoniso->getWeight(std::abs(eta[i]),pt[i]));
        }
        return wVec;
    };

    auto muonSFTrg = [this, _muontrg](floats &pt, floats &eta)->std::vector<float> {
        std::vector<float> wVec;
        if (pt.size() > 0) {
            for (unsigned int i=0; i<pt.size(); i++)
                wVec.emplace_back(_muontrg->getWeight(std::abs(eta[i]),pt[i]));
        }
        return wVec;
    };

    _rlm = _rlm.Define("muonWeightId", muonSFId, {"Muon_pt","Muon_eta"})
               .Define("muonWeightIso", muonSFIso, {"Muon_pt","Muon_eta"})
               .Define("muonWeightTrg", muonSFTrg, {"Muon_pt","Muon_eta"});


    // Tau SF
    cout << "Loading Tau SF" << endl;
    std::string tauid_vse = "VLoose";
    std::string tauid_vsmu = "Tight";
    std::string tauid_vsjet = "VTight";

    cout << "Tau ID WP vsJet : " << tauid_vsjet << endl;
    cout << "Tau ID WP vsMuon : " << tauid_vsmu << endl;
    cout << "Tau ID WP vsElectron : " << tauid_vse << endl;

    TauIDSFTool* _tauidSFjet;
    TauIDSFTool* _tauidSFele;
    TauIDSFTool* _tauidSFmu;
    TauESTool* _testool;
    TauFESTool* _festool;
    std::string tauYear = "";

    if (_isRun16pre) {
        tauYear = "UL2016_preVFP";
    } else if (_isRun16post) {
        tauYear = "UL2016_postVFP";
    } else {
        tauYear = "UL" + _year;
    }
    _tauidSFjet = new TauIDSFTool(tauYear, "DeepTau2017v2p1VSjet", tauid_vsjet);
    _tauidSFele = new TauIDSFTool(tauYear, "DeepTau2017v2p1VSe", tauid_vse);
    _tauidSFmu = new TauIDSFTool(tauYear, "DeepTau2017v2p1VSmu", tauid_vsmu);
    _testool = new TauESTool(tauYear, "DeepTau2017v2p1VSjet");
    _festool = new TauFESTool(tauYear);

    auto tauSFIdVsJet = [this, _tauidSFjet](floats &pt, floats &eta, uchars &genid)->std::vector<float> {
        std::vector<float> wVec;
        if (pt.size() > 0) {
            for (unsigned int i=0; i<pt.size(); i++)
                wVec.emplace_back(_tauidSFjet->getSFvsPT(pt[i], int(genid[i])));
        }
        return wVec;
    };

    auto tauSFIdVsEl = [this, _tauidSFele](floats &pt, floats &eta, uchars &genid)->std::vector<float> {
        std::vector<float> wVec;
        if (pt.size() > 0) {
            for (unsigned int i=0; i<pt.size(); i++)
                wVec.emplace_back(_tauidSFele->getSFvsEta(abs(eta[i]), int(genid[i])));
        }
        return wVec;
    };

    auto tauSFIdVsMu = [this, _tauidSFmu](floats &pt, floats &eta, uchars &genid)->std::vector<float> {
        std::vector<float> wVec;
        if (pt.size() > 0) {
            for (unsigned int i=0; i<pt.size(); i++)
                wVec.emplace_back(_tauidSFmu->getSFvsEta(abs(eta[i]), int(genid[i])));
        }
        return wVec;
    };

    _rlm = _rlm.Define("tauWeightIdVsJet", tauSFIdVsJet, {"Tau_pt","Tau_eta","Tau_genPartFlav"})
               .Define("tauWeightIdVsEl", tauSFIdVsEl, {"Tau_pt","Tau_eta","Tau_genPartFlav"})
               .Define("tauWeightIdVsMu", tauSFIdVsMu, {"Tau_pt","Tau_eta","Tau_genPartFlav"});

    // Tau ES
    cout<<"Applying TauES on Genuine taus"<<endl;
    auto tauES = [this, _testool, _festool](floats &pt, floats &eta, ints &dm, uchars &genid, floats &x)->floats {
        floats xout;
        for (unsigned int i=0; i<pt.size(); i++) {
            float es = 1.0;
            if (genid[i]==5) {
                es = _testool->getTES(pt[i], dm[i], genid[i]);
            } else if (genid[i]==1 || genid[i]==3){
                es = _festool->getFES(eta[i], dm[i], genid[i]);
            }
            xout.emplace_back(x[i]*es);
        }
        return xout;
    };

    _rlm = _rlm.Redefine("Tau_pt", tauES, {"Tau_pt", "Tau_eta", "Tau_decayMode", "Tau_genPartFlav", "Tau_pt"})
               .Redefine("Tau_mass", tauES, {"Tau_pt", "Tau_eta", "Tau_decayMode", "Tau_genPartFlav", "Tau_mass"});
}

/*
bool NanoAODAnalyzerrdframe::helper_1DHistCreator(std::string hname, std::string title, const int nbins, const double xlow, const double xhi, std::string rdfvar, std::string evWeight)
{
	RDF1DHist histojets = _rlm.Histo1D({hname.c_str(), title.c_str(), nbins, xlow, xhi}, rdfvar, evWeight); // Fill with weight given by evWeight
	_th1dhistos[hname] = histojets;
}
*/

void NanoAODAnalyzerrdframe::helper_1DHistCreator(std::string hname, std::string title, const int nbins, const double xlow, const double xhi, std::string rdfvar, std::string evWeight, RNode *anode)
{
	RDF1DHist histojets = anode->Histo1D({hname.c_str(), title.c_str(), nbins, xlow, xhi}, rdfvar, evWeight); // Fill with weight given by evWeight
	_th1dhistos[hname] = histojets;
}

// Automatically loop to create
void NanoAODAnalyzerrdframe::setupCuts_and_Hists()
{
	cout << "setting up definitions, cuts, and histograms" <<endl;

	for ( auto &c : _varinfovector)
	{
		if (c.mincutstep.length()==0) _rlm = _rlm.Define(c.varname, c.vardefinition);
	}

	for (auto &x : _hist1dinfovector)
	{
		std::string hpost = "";

		if (x.mincutstep.length()==0)
		{
			helper_1DHistCreator(std::string(x.hmodel.fName)+hpost,  std::string(x.hmodel.fTitle)+hpost, x.hmodel.fNbinsX, x.hmodel.fXLow, x.hmodel.fXUp, x.varname, x.weightname, &_rlm);
		}
	}

	_rnt.setRNode(&_rlm);

	for (auto acut : _cutinfovector)
	{
    std::string cutname = "S" + to_string(acut.idx.length()-1);
		std::string hpost = "_"+cutname;
		RNode *r = _rnt.getParent(acut.idx)->getRNode();
		auto rnext = new RNode(r->Define(cutname, acut.cutdefinition));
		*rnext = rnext->Filter(cutname);

		for ( auto &c : _varinfovector)
		{
			if (acut.idx.compare(c.mincutstep)==0) *rnext = rnext->Define(c.varname, c.vardefinition);
		}
		for (auto &x : _hist1dinfovector)
		{
			if (acut.idx.compare(0, x.mincutstep.length(), x.mincutstep)==0)
			{
				helper_1DHistCreator(std::string(x.hmodel.fName)+hpost,  std::string(x.hmodel.fTitle)+hpost, x.hmodel.fNbinsX, x.hmodel.fXLow, x.hmodel.fXUp, x.varname, x.weightname, rnext);
			}
		}
		_rnt.addDaughter(rnext, acut.idx);

		/*
		_rlm = _rlm.Define(cutname, acut.cutdefinition);
		_rlm = _rlm.Filter(cutname);

		for ( auto &c : _varinfovector)
		{
			if (acut.idx.compare(c.mincutstep)==0) _rlm = _rlm.Define(c.varname, c.vardefinition);
		}
		for (auto &x : _hist1dinfovector)
		{
			if (acut.idx.compare(0, x.mincutstep.length(), x.mincutstep)==0)
			{
				helper_1DHistCreator(std::string(x.hmodel.fName)+hpost,  std::string(x.hmodel.fTitle)+hpost, x.hmodel.fNbinsX, x.hmodel.fXLow, x.hmodel.fXUp, x.varname, x.weightname);
			}
		}
		_rnt.addDaughter(&_rlm, acut.idx);
		*/
	}
}

void NanoAODAnalyzerrdframe::add1DHist(TH1DModel histdef, std::string variable, std::string weight,string mincutstep)
{
	_hist1dinfovector.push_back({histdef, variable, weight, mincutstep});
}


void NanoAODAnalyzerrdframe::drawHists(RNode t)
{
	cout << "processing" <<endl;
	t.Count();
}

void NanoAODAnalyzerrdframe::addVar(varinfo v)
{
	_varinfovector.push_back(v);
}

void NanoAODAnalyzerrdframe::addVartoStore(string varname)
{
	// varname is assumed to be a regular expression.
	// e.g. if varname is "Muon_eta" then "Muon_eta" will be stored
	// if varname=="Muon_.*", then any branch name that starts with "Muon_" string will
	// be saved
	_varstostore.push_back(varname);
	/*
	std::regex b(varname);
	bool foundmatch = false;
	for (auto a: _rlm.GetColumnNames())
	{
		if (std::regex_match(a, b)) {
			_varstostore.push_back(a);
			foundmatch = true;
		}
	}
	*/

}

void NanoAODAnalyzerrdframe::setupTree()
{
	vector<RNodeTree *> rntends;
	_rnt.getRNodeLeafs(rntends);
	for (auto arnt: rntends)
	{
		RNode *arnode = arnt->getRNode();
		string nodename = arnt->getIndex();
		vector<string> varforthistree;
		std::map<string, int> varused;

		for (auto varname: _varstostore)
		{
			bool foundmatch = false;
			std::regex b(varname);
			for (auto a: arnode->GetColumnNames())
			{
				if (std::regex_match(a, b) && varused[a]==0)
				{
					varforthistree.push_back(a);
					varused[a]++;
					foundmatch = true;
				}
			}
			if (!foundmatch)
			{
				cout << varname << " not found at "<< nodename << endl;
			}

		}
		_varstostorepertree[nodename]  = varforthistree;
	}

}

void NanoAODAnalyzerrdframe::addCuts(string cut, string idx)
{
	_cutinfovector.push_back({cut, idx});
}


void NanoAODAnalyzerrdframe::run(bool saveAll, string outtreename)
{
	/*
	if (saveAll) {
		_rlm.Snapshot(outtreename, _outfilename);
	}
	else {
		// use the following if you want to store only a few variables
		_rlm.Snapshot(outtreename, _outfilename, _varstostore);
	}
	*/

	vector<RNodeTree *> rntends;
	_rnt.getRNodeLeafs(rntends);
	_rnt.Print();
        cout << rntends.size() << endl;
	// on master, regex_replace doesn't work somehow
	//std::regex rootextension("\\.root");

	for (auto arnt: rntends)
	{
		string nodename = arnt->getIndex();
		//string outname = std::regex_replace(_outfilename, rootextension, "_"+nodename+".root");
		string outname = _outfilename;
		// if producing many root files due to branched selection criteria,  each root file will get a different name
		if (rntends.size()>1) outname.replace(outname.find(".root"), 5, "_"+nodename+".root");
		_outrootfilenames.push_back(outname);
		RNode *arnode = arnt->getRNode();
                cout << arnt->getIndex();
		//cout << ROOT::RDF::SaveGraph(_rlm) << endl;
		if (saveAll) {
			arnode->Snapshot(outtreename, outname);
		}
		else {
			// use the following if you want to store only a few variables
			//arnode->Snapshot(outtreename, outname, _varstostore);
			cout << " writing branches" << endl;
			for (auto bname: _varstostorepertree[nodename])
			{
				cout << bname << ", ";
			}
                        cout<<endl;
			arnode->Snapshot(outtreename, outname, _varstostorepertree[nodename]);
		}
                _outrootfile = new TFile(outname.c_str(),"UPDATE");
                for (auto &h : _th1dhistos)
                {
                        if (h.second.GetPtr() != nullptr){
                            h.second.GetPtr()->Print();
                            h.second.GetPtr()->Write();
                            //std::cout<<h.second->GetName()<<std::endl;
                            //h.second->Write();
                            //std::cout<<"Histogram is written"<<std::endl;
                        }
                }
                _outrootfile->Write(0, TObject::kOverwrite);
                _outrootfile->Close();
	}
}
