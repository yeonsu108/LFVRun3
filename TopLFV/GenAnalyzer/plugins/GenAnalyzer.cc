// -*- C++ -*-
//
// Package:    TopLFV/GenAnalyzer
// Class:      GenAnalyzer
//
/**\class GenAnalyzer GenAnalyzer.cc TopLFV/GenAnalyzer/plugins/GenAnalyzer.cc

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

class GenAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit GenAnalyzer(const edm::ParameterSet&);
  ~GenAnalyzer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  edm::EDGetTokenT<reco::GenParticleCollection> genParticleLabel_; 
  // ----------member data ---------------------------
  TH1D *h_lepLFVdR;
  TH1D *h_lepLFVdPhi;
  
  TH1D *h_cLFVpt;
  TH1D *h_bSMpt;
  TH1D *h_muLFVpt;
  TH1D *h_tauLFVpt;

  TH1D *h_cLFVeta;
  TH1D *h_bSMeta;
  TH1D *h_muLFVeta;
  TH1D *h_tauLFVeta;

  float lepLFVdR;
  float lepLFVdPhi;

  float cLFVpt;
  float bSMpt;
  float muLFVpt;
  float tauLFVpt;
  
  float cLFVeta;
  float bSMeta;
  float muLFVeta;
  float tauLFVeta;
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
GenAnalyzer::GenAnalyzer(const edm::ParameterSet& iConfig)
    : genParticleLabel_(consumes<reco::GenParticleCollection>(iConfig.getUntrackedParameter<edm::InputTag>("genParticleLabel"))) {

  edm::Service<TFileService> fs;
  h_lepLFVdR = fs->make<TH1D>("lepLFVdR","DeltaR between two leptons",30,0.0,6.0);
  //h_lepLFVdPhi = fs->make<TH1D>("lepLFVdR","DeltaPhi between two leptons",40,-4.0,4.0);
  
  h_cLFVpt = fs->make<TH1D>("cLFVpt","Pt of LFV c quark",30,0.0,300);
  h_bSMpt = fs->make<TH1D>("bSMpt","Pt of SM b quark",30,0.0,300);
  h_muLFVpt = fs->make<TH1D>("muLFVpt","Pt of LFV muon",30,0.0,300);
  h_tauLFVpt = fs->make<TH1D>("tauLFVpt","Pt of LFV tau",30,0.0,300);

  h_cLFVeta = fs->make<TH1D>("cLFVeta","Eta of LFV c quark",20,-4.0,4.0);
  h_bSMeta = fs->make<TH1D>("bSMeta","Eta of SM b quark",20,-4.0,4.0);
  h_muLFVeta = fs->make<TH1D>("muLFVeta","Eta of LFV muon",20,-4.0,4.0);
  h_tauLFVeta = fs->make<TH1D>("tauLFVeta","Eta of LFV tau",20,-4.0,4.0);

}

GenAnalyzer::~GenAnalyzer() {
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  //
  // please remove this method altogether if it would be left empty
}

//
// member functions
//

// ------------ method called for each event  ------------
void GenAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;
  using namespace std;
  
  Handle<reco::GenParticleCollection> genParticles;
  iEvent.getByToken(genParticleLabel_, genParticles);
  
  math::XYZTLorentzVector muonfromLFVTop;
  math::XYZTLorentzVector taufromLFVTop;
  math::XYZTLorentzVector cfromLFVTop;
  math::XYZTLorentzVector bfromSMTop;
  
  lepLFVdR      =   -1;
  lepLFVdPhi    =   999;

  cLFVpt        =   -1;
  bSMpt         =   -1;
  muLFVpt       =   -1;
  tauLFVpt      =   -1;

  cLFVeta       =   6;
  bSMeta        =   6;
  muLFVeta      =   6;
  tauLFVeta     =   6;

  int nmu = 0;
  int ntau = 0;
  int nb = 0;
  int nc = 0;

  for (const auto& genp : *genParticles) {
    int id = genp.pdgId();
    //cout<<"pdgid : "<< id <<endl;
    auto momp = genp.mother();
    //cout<<"mom particle : "<< momp <<endl;
    if( momp == 0 ) continue;
    int momid = momp->pdgId();
    //cout<<"Pdg id : "<<id<<" Mom pdgid : "<<momid<<endl;
    bool iscfromLFVTop = (abs(momid) == 6) && (abs(id) == 4);
    bool ismufromLFVTop = (abs(momid) == 6) && (abs(id) == 13);
    bool istaufromLFVTop = (abs(momid) == 6) && (abs(id) == 15);
    bool isbfromSMTop = (abs(momid) == 6) && (abs(id) == 5);
    if( iscfromLFVTop || ismufromLFVTop || istaufromLFVTop || isbfromSMTop ){
        //cout<<"c from LFV Top : "<<iscfromLFVTop<<endl;
        //cout<<"b from SM Top : "<<isbfromSMTop<<endl;
        //cout<<"mu from LFV Top : "<<ismufromLFVTop<<endl;
        //cout<<"tau from LFV Top : "<<istaufromLFVTop<<endl;
    }
    
    if ( ismufromLFVTop ){
        nmu++;
        muonfromLFVTop = genp.p4();
    } else if ( istaufromLFVTop ){
        ntau++;
        taufromLFVTop = genp.p4();
    } else if ( iscfromLFVTop){
        nc++;
        cfromLFVTop = genp.p4();
    } else if ( isbfromSMTop ){
        nb++;
        bfromSMTop = genp.p4();
    } else continue;


    //std::cout << "Pdg Id = " << id << " pt = " << pt << std::endl;
    
    // do something with track parameters, e.g, plot the charge.
    // int charge = track.charge();
  }
  cout<<"# of b : "<<nb<<" # of c : "<<nc<<" # of muon : "<<nmu<<" # of tau : "<<ntau<<endl;
  lepLFVdR = reco::deltaR(muonfromLFVTop, taufromLFVTop);
  //lepLFVdPhi = reco::deltaPhi(muonfromLFVTop, taufromLFVTop);
  
  cLFVpt = cfromLFVTop.Pt();
  bSMpt = bfromSMTop.Pt();
  muLFVpt = muonfromLFVTop.Pt();
  tauLFVpt = taufromLFVTop.Pt();

  cLFVeta = cfromLFVTop.Eta();
  bSMeta = bfromSMTop.Eta();
  muLFVeta = muonfromLFVTop.Eta();
  tauLFVeta = taufromLFVTop.Eta();

  cout<<endl;
  cout<<"LFV c pt : "<< cLFVpt << ", SM b pt : "<< bSMpt << endl;
  cout<<"LFV muon pt : "<< muLFVpt <<", LFV tau pt"<< tauLFVpt << endl;
  cout<<endl;

  h_lepLFVdR->Fill(lepLFVdR);
  //h_lepLFVdPhi->Fill(lepLFVdPhi);
  
  h_cLFVpt->Fill(cLFVpt);
  h_bSMpt->Fill(bSMpt);
  h_muLFVpt->Fill(muLFVpt);
  h_tauLFVpt->Fill(tauLFVpt);
  
  h_cLFVeta->Fill(cLFVeta);
  h_bSMeta->Fill(bSMeta);
  h_muLFVeta->Fill(muLFVeta);
  h_tauLFVeta->Fill(tauLFVeta);
}

// ------------ method called once each job just before starting event loop  ------------
void GenAnalyzer::beginJob() {
  // please remove this method if not needed
}

// ------------ method called once each job just after ending the event loop  ------------
void GenAnalyzer::endJob() {
  // please remove this method if not needed
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void GenAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
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
DEFINE_FWK_MODULE(GenAnalyzer);
