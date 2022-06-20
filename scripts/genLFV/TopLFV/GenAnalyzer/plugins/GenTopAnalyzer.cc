// -*- C++ -*-
//
// Package:    TopLFV/GenTopAnalyzer
// Class:      GenTopAnalyzer
//
/**\class GenTopAnalyzer GenTopAnalyzer.cc TopLFV/GenTopAnalyzer/plugins/GenTopAnalyzer.cc

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

class GenTopAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources> {
public:
  explicit GenTopAnalyzer(const edm::ParameterSet&);
  ~GenTopAnalyzer();

  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  void beginJob() override;
  void analyze(const edm::Event&, const edm::EventSetup&) override;
  void endJob() override;

  edm::EDGetTokenT<reco::GenParticleCollection> genParticleLabel_; 
  // ----------member data ---------------------------
  TH1D *h_lepdR;
  TH1D *h_lepmass;

  TH1D *h_cpt;
  TH1D *h_bpt;
  TH1D *h_lep1pt;
  TH1D *h_lep2pt;

  TH1D *h_ceta;
  TH1D *h_beta;
  TH1D *h_lep1eta;
  TH1D *h_lep2eta;
  
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

  float cpt;
  float bpt;
  float lep1pt;
  float lep2pt;
  
  float ceta;
  float beta;
  float lep1eta;
  float lep2eta;

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
GenTopAnalyzer::GenTopAnalyzer(const edm::ParameterSet& iConfig)
    : genParticleLabel_(consumes<reco::GenParticleCollection>(iConfig.getUntrackedParameter<edm::InputTag>("genParticleLabel"))) {

  edm::Service<TFileService> fs;
  h_lepdR = fs->make<TH1D>("lepdR","DeltaR between two leptons",12,0.0,6.0);
  h_lepmass = fs->make<TH1D>("lepmass","Inv. mass between two leptons",20,0.0,400);

  h_cpt = fs->make<TH1D>("cpt","Pt of c quark",30,0.0,300);
  h_bpt = fs->make<TH1D>("bpt","Pt of b quark",30,0.0,300);
  h_lep1pt = fs->make<TH1D>("lep1pt","Pt of leading lepton",30,0.0,300);
  h_lep2pt = fs->make<TH1D>("lep2pt","Pt of sub-leading lepton",30,0.0,300);

  h_ceta = fs->make<TH1D>("ceta","Eta of c quark",20,-4.0,4.0);
  h_beta = fs->make<TH1D>("beta","Eta of b quark",20,-4.0,4.0);
  h_lep1eta = fs->make<TH1D>("lep1eta","Eta of leading lepton",20,-4.0,4.0);
  h_lep2eta = fs->make<TH1D>("lep2eta","Eta of sub-leading lepton",20,-4.0,4.0);
  
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

GenTopAnalyzer::~GenTopAnalyzer() {
  // do anything here that needs to be done at desctruction time
  // (e.g. close files, deallocate resources etc.)
  //
  // please remove this method altogether if it would be left empty
}

//
// member functions
//

// ------------ method called for each event  ------------
void GenTopAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup) {
  using namespace edm;
  using namespace std;
  
  Handle<reco::GenParticleCollection> genParticles;
  iEvent.getByToken(genParticleLabel_, genParticles);
  
  math::XYZTLorentzVector LFVTop;
  math::XYZTLorentzVector LepTop;
  math::XYZTLorentzVector HadTop;
  math::XYZTLorentzVector bquark;
  math::XYZTLorentzVector cquark;
  math::XYZTLorentzVector lep1;
  math::XYZTLorentzVector lep2;
  
  lepdR         =   -1;
  lepmass       =   -1;

  cpt           =   -1;
  bpt           =   -1;
  lep1pt        =   -1;
  lep2pt        =   -1;

  ceta          =   6;
  beta          =   6;
  lep1eta       =   6;
  lep2eta       =   6;

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
  std::vector<reco::GenParticle> leptons;
  std::vector<math::XYZTLorentzVector> bquarks;
  std::vector<math::XYZTLorentzVector> cquarks;
  for (const auto& genp : *genParticles) {
    int id = genp.pdgId();
    auto momp = genp.mother();
    if( momp == 0 ) continue;
    int momid = momp->pdgId();
    bool islepton = abs(id) == 11 || abs(id) == 13 || abs(id) == 15;
    auto dau1p = genp.daughter(0);
    auto dau2p = genp.daughter(1);
    if ( abs(id) == 6 && (dau1p != 0 && dau2p != 0)){
        //cout<<endl;
        int dau1id = dau1p->pdgId();
        int dau2id = dau2p->pdgId();
        //cout<<"d1 id : "<<dau1id<<" d2 id : "<<dau2id<<endl;
        if (abs(dau1p->pdgId()) == 24 || abs(dau2p->pdgId()) == 24){
            while (true){
                if (abs(dau1id) == 24){
                    dau1p = dau1p->daughter(0);
                    dau1id = dau1p->pdgId();
                    //cout<<"update d1 id : "<<dau1id<<" d2 id : "<<dau2id<<endl;
                }
                if (abs(dau2id) == 24){
                    dau2p = dau2p->daughter(0);
                    dau2id = dau2p->pdgId();
                    //cout<<"d1 id : "<<dau1id<<" update d2 id : "<<dau2id<<endl;
                }
                if (abs(dau1id) != 24 && abs(dau2id) != 24) break;
            }
            cout<<endl;
            if ( (abs(dau1id) >= 11 && abs(dau1id) <= 16) || (abs(dau2id) >= 11 && abs(dau2id) <= 16) ){
                //cout<<"Leptonic Top"<<endl;
                //cout<<"ID : "<<id<<" d1 ID : "<<dau1id<<" d2 ID : "<<dau2id<<endl;
                LepTop = genp.p4();
                ntoplep++;
            } else {
                //cout<<"Hadronic Top"<<endl;
                //cout<<"ID : "<<id<<" d1 ID : "<<dau1id<<" d2 ID : "<<dau2id<<endl;
                HadTop = genp.p4();
                ntophad++;
            }
        } else if (abs(dau1id) == 4 || abs(dau2id) == 4){
            //cout<<"LFV Top"<<endl;
            //cout<<"ID : "<<id<<" d1 ID : "<<dau1id<<" d2 ID : "<<dau2id<<endl;
            LFVTop = genp.p4();
            ntoplfv++;
        }
    }
    if (islepton && (genp.isPromptDecayed() || genp.isPromptFinalState())){
        //leptons.emplace_back(genp.p4());
        leptons.emplace_back(genp);
        nlep++;
        if (abs(id) == 11) nelec++;
        else if (abs(id) == 13) nmu++;
        else if (abs(id) == 15) ntau++;
    }
    if ( abs(id) == 5 ){
        bquarks.emplace_back(genp.p4());
        nb++;
    }
    if ( abs(id) == 4 ){
        cquarks.emplace_back(genp.p4());
        nc++;
    }
  }

  float pt1 = -1;
  float pt2 = -1;
  for ( auto lep : leptons ){
      int lep1id = 0;
      int lep2id = 0;
      cout<<"lep pt : "<<lep.p4().Pt()<<endl;
      if (lep.p4().Pt() > pt1 && lep1id != lep.pdgId()){
          lep2 = lep1;
          lep2id = lep1id;
          lep1 = lep.p4();
          lep1id = lep.pdgId();
      } else if (lep.p4().Pt() > pt2 && lep.p4().Pt() < pt1 && lep1id != lep.pdgId()){
          lep2 = lep.p4();
          lep2id = lep.pdgId();
      }
      pt1 = lep1.Pt();
      pt2 = lep2.Pt();
      cout<<"pt1 : "<<pt1<<", id : "<<lep1id<<" pt2 : "<<pt2<<", id : "<<lep2id<<endl;
  }
  pt1 = -1;
  for ( auto bq : bquarks ){
      if (bq.Pt() > pt1){
          bquark = bq;
          pt1 = bq.Pt();
      }
  }
  pt1 = -1;
  for ( auto cq : cquarks ){
      if (cq.Pt() > pt1){
          cquark = cq;
          pt1 = cq.Pt();
      }
  }
  cout<<nlep<<" leptons, "<<nelec<<" electrons, "<<nmu<<" muons, "<<ntau<<" taus"<<endl;
  cout<<ntop<<" tops, "<<ntoplfv<<" LFV, "<<ntoplep<<" leptonic, "<<ntophad<<" hadronic"<<endl;
  cout<<nb<<" bquarks, "<<nc<<" cquarks"<<endl;

  lepdR = reco::deltaR(lep1, lep2);
  lepmass = (lep1 + lep2).M();
  
  cpt = cquark.Pt();
  bpt = bquark.Pt();
  lep1pt = lep1.Pt();
  lep2pt = lep2.Pt();

  ceta = cquark.Eta();
  beta = bquark.Eta();
  lep1eta = lep1.Eta();
  lep2eta = lep2.Eta();

  if(ntoplfv > 0){
      topLFVpt = LFVTop.Pt();
      topLFVeta = LFVTop.Eta();
      topLFVmass = LFVTop.M();
  }
  if(ntoplep > 0){
      toplep_pt = LepTop.Pt();
      toplep_eta = LepTop.Eta();
      toplep_mass = LepTop.M();
  }
  if(ntophad > 0){
      tophad_pt = HadTop.Pt();
      tophad_eta = HadTop.Eta();
      tophad_mass = HadTop.M();
  }

  h_lepdR->Fill(lepdR);
  h_lepmass->Fill(lepmass);
  
  h_cpt->Fill(cpt);
  h_bpt->Fill(bpt);
  h_lep1pt->Fill(lep1pt);
  h_lep2pt->Fill(lep2pt);
  
  h_ceta->Fill(ceta);
  h_beta->Fill(beta);
  h_lep1eta->Fill(lep1eta);
  h_lep2eta->Fill(lep2eta);

  h_topLFVpt->Fill(topLFVpt);
  h_topLFVeta->Fill(topLFVeta);
  h_topLFVmass->Fill(topLFVmass);
  h_toplep_pt->Fill(toplep_pt);
  h_toplep_eta->Fill(toplep_eta);
  h_toplep_mass->Fill(toplep_mass);
  h_tophad_pt->Fill(tophad_pt);
  h_tophad_eta->Fill(tophad_eta);
  h_tophad_mass->Fill(tophad_mass);
}

// ------------ method called once each job just before starting event loop  ------------
void GenTopAnalyzer::beginJob() {
  // please remove this method if not needed
}

// ------------ method called once each job just after ending the event loop  ------------
void GenTopAnalyzer::endJob() {
  // please remove this method if not needed
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void GenTopAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
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
DEFINE_FWK_MODULE(GenTopAnalyzer);
