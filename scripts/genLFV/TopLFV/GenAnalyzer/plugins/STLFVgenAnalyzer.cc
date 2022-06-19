// -*- C++ -*-
//
// Package:    TopLFV/STLFVgenAnalyzer
// Class:      STLFVgenAnalyzer
//
/**\class STLFVgenAnalyzer STLFVgenAnalyzer.cc TopLFV/STLFVgenAnalyzer/plugins/STLFVgenAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Jongwon Lim
//         Created:  Sun, 23 Aug 2020 20:47:02 GMT
//
//

// system include files
#include <memory>

// user include files
  
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "DataFormats/Common/interface/Association.h"
#include "DataFormats/Common/interface/RefToPtr.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "CommonTools/UtilAlgos/interface/StringCutObjectSelector.h"

#include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"

#include "TH1.h"
#include "TLorentzVector.h"

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.

using namespace edm;
using namespace reco;

class STLFVgenAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit STLFVgenAnalyzer(const edm::ParameterSet&);
  ~STLFVgenAnalyzer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  edm::EDGetTokenT<reco::GenParticleCollection> genParticleLabel_; 
  // ----------member data ---------------------------
  TH1D *h_lepdR;
  TH1D *h_lepmass;

  TH1D *h_upt;
  TH1D *h_bpt;
  TH1D *h_mupt;
  TH1D *h_taupt;

  TH1D *h_ueta;
  TH1D *h_beta;
  TH1D *h_mueta;
  TH1D *h_taueta;
  
  TH1D *h_topLFVpt;
  TH1D *h_topLFVeta;
  TH1D *h_topLFVmass;
  TH1D *h_toplep_pt;
  TH1D *h_toplep_eta;
  TH1D *h_toplep_mass;
  TH1D *h_tophad_pt;
  TH1D *h_tophad_eta;
  TH1D *h_tophad_mass;

  float lepdR;
  float lepmass;

  float upt;
  float bpt;
  float mupt;
  float taupt;
  
  float ueta;
  float beta;
  float mueta;
  float taueta;

  float topLFVpt;
  float topLFVeta;
  float topLFVmass;
  float toplep_pt;
  float toplep_eta;
  float toplep_mass;
  float tophad_pt;
  float tophad_eta;
  float tophad_mass;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
STLFVgenAnalyzer::STLFVgenAnalyzer(const edm::ParameterSet& iConfig)
    : genParticleLabel_(consumes<reco::GenParticleCollection>(iConfig.getUntrackedParameter<edm::InputTag>("genParticleLabel"))) {

  edm::Service<TFileService> fs;
  h_lepdR = fs->make<TH1D>("lepdR","DeltaR between two leptons",24,0.0,6.0);
  h_lepmass = fs->make<TH1D>("lepmass","Inv. mass between two leptons",20,0.0,400);

  h_upt = fs->make<TH1D>("cpt","Up-type quark pt",40,0.0,400);
  h_bpt = fs->make<TH1D>("bpt","B quark pt",40,0.0,400);
  h_mupt = fs->make<TH1D>("mupt","Muon pt",40,0.0,400);
  h_taupt = fs->make<TH1D>("taupt","Tau pt",40,0.0,400);

  h_ueta = fs->make<TH1D>("ceta","Up-type quark eta",20,-4.0,4.0);
  h_beta = fs->make<TH1D>("beta","B quark eta",20,-4.0,4.0);
  h_mueta = fs->make<TH1D>("mueta","Muon eta",20,-4.0,4.0);
  h_taueta = fs->make<TH1D>("taueta","Tau eta",20,-4.0,4.0);
  
  h_topLFVpt = fs->make<TH1D>("topLFVpt","Pt of LFV top",30,0.0,300);
  h_topLFVeta = fs->make<TH1D>("topLFVeta","Eta of LFV top",20,-4.0,4.0);
  h_topLFVmass = fs->make<TH1D>("topLFVmass","mass of LFV top",50,150,200);
  h_toplep_pt = fs->make<TH1D>("toplep_pt","Pt of leptonic top",30,0.0,300);
  h_toplep_eta = fs->make<TH1D>("toplep_eta","Eta of leptonic top",20,-4.0,4.0);
  h_toplep_mass = fs->make<TH1D>("toplep_mass","mass of leptonic top",50,150,200);
  h_tophad_pt = fs->make<TH1D>("tophad_pt","Pt of hadronic top",30,0.0,300);
  h_tophad_eta = fs->make<TH1D>("tophad_eta","Eta of hadronic top",20,-4.0,4.0);
  h_tophad_mass = fs->make<TH1D>("tophad_mass","mass of hadronic top",50,150,200);

}

STLFVgenAnalyzer::~STLFVgenAnalyzer() {
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  //
  // please remove this method altogether if it would be left empty
}

//
// member functions
//

// ------------ method called for each event  ------------
void STLFVgenAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;
  using namespace std;
  
  Handle<reco::GenParticleCollection> genParticles;
  iEvent.getByToken(genParticleLabel_, genParticles);
  
  
  lepdR         =   -1;
  lepmass       =   -1;

  upt           =   -1;
  bpt           =   -1;
  mupt        =   -1;
  taupt        =   -1;

  ueta          =   6;
  beta          =   6;
  mueta       =   6;
  taueta       =   6;

  topLFVpt          =   -1;
  topLFVeta         =   10;
  topLFVmass        =   -1;
  toplep_pt     =   -1;
  toplep_eta    =   10;
  toplep_mass   =   -1;
  tophad_pt     =   -1;
  tophad_eta    =   10;
  tophad_mass   =   -1;

  int nb = 0;
  int nc = 0;
  int nlep = 0;
  int nelec = 0;
  int nmu = 0;
  int ntau = 0;
  int ntop = 0;
  int ntoplep = 0;
  int ntophad = 0;
  int ntoplfv = 0;

  //std::vector<math::XYZTLorentzVector> leptons;
  cout<<"##############################################"<<endl;
  math::XYZTLorentzVector bquark;
  math::XYZTLorentzVector Tau;
  math::XYZTLorentzVector Mu;

  for (const auto& genp : *genParticles) {
    int id = genp.pdgId();
    auto momp = genp.mother();
    if( momp == 0 ) continue;
    int momid = momp->pdgId();
    bool islepton = abs(id) == 11 || abs(id) == 13 || abs(id) == 15;
    bool isMuTau = (abs(id) == 13 || abs(id) == 15) && (genp.isPromptDecayed() || genp.isPromptFinalState());
    /*
    if ((abs(id) == 4 || abs(id) == 2) && genp.numberOfDaughters() == 3){
        auto dau1p = genp.daughter(0);
        auto dau2p = genp.daughter(1);
        auto dau3p = genp.daughter(2);
        int dau1id = dau1p->pdgId();
        int dau2id = dau2p->pdgId();
        int dau3id = dau3p->pdgId();
        if(abs(dau1id)==6||abs(dau1id)==13||abs(dau1id)==15){
            cout<< "Number of Daughters : "<< genp.numberOfDaughters() << endl;
            cout<<"P  : "<<id<<endl;
            cout<<"D1 : "<<dau1id<<endl;
            cout<<"D2 : "<<dau2id<<endl;
            cout<<"D3 : "<<dau3id<<endl;
            if(abs(dau1id)==13) Mu = dau1p->p4();
            else if(abs(dau2id)==13) Mu = dau2p->p4();
            else if(abs(dau3id)==13) Mu = dau3p->p4();
            
            if(abs(dau1id)==15) Tau = dau1p->p4();
            else if(abs(dau2id)==15) Tau = dau2p->p4();
            else if(abs(dau3id)==15) Tau = dau3p->p4();
        }
    }*/
    if(isMuTau){
        if(abs(id) == 13){
            cout<<"Muon"<<endl;
            Mu = genp.p4();
            nmu++;
        }
        if(abs(id) == 15){
            cout<<"Tau"<<endl;
            Tau = genp.p4();
            ntau++;
        }
    }
    if(abs(id) == 6 && genp.numberOfDaughters() == 2){
        auto dau1p = genp.daughter(0);
        auto dau2p = genp.daughter(1);
        int dau1id = dau1p->pdgId();
        int dau2id = dau2p->pdgId();
        if(abs(dau1id) == 5) bquark = dau1p->p4();
        else if(abs(dau2id) == 5) bquark = dau2p->p4();
    }

  }
  if(nmu==1 && ntau==1){

      mupt = Mu.Pt();
      taupt = Tau.Pt();
      bpt = bquark.Pt();
      mueta = Mu.Eta();
      taueta = Tau.Eta();
      beta = bquark.Eta();
      
      lepdR = reco::deltaR(Mu, Tau);
      lepmass = (Mu + Tau).M();
      
      h_lepdR->Fill(lepdR);
      h_lepmass->Fill(lepmass);
      
      h_bpt->Fill(bpt);
      h_mupt->Fill(mupt);
      h_taupt->Fill(taupt);
      
      h_beta->Fill(beta);
      h_mueta->Fill(mueta);
      h_taueta->Fill(taueta);
  }
  return;
}

// ------------ method called once each job just before starting event loop  ------------
void STLFVgenAnalyzer::beginJob() {
  // please remove this method if not needed
}

// ------------ method called once each job just after ending the event loop  ------------
void STLFVgenAnalyzer::endJob() {
  // please remove this method if not needed
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void STLFVgenAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(STLFVgenAnalyzer);
