#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"
#include "ROOT/RDF/RInterface.hxx"
#include "TCanvas.h"
#include "TH1D.h"
#include "TLatex.h"
#include "TLegend.h"
#include "Math/Vector4Dfwd.h"
#include "TStyle.h"
#include <vector>
#include "TLorentzVector.h"

using namespace ROOT::VecOps;
using floats = RVec<float>;
using bools = RVec<bool>;
using ints = RVec<int>;
using FourVector = ROOT::Math::PtEtaPhiMVector;
using FourVectorVec = std::vector<FourVector>;

ints find_element(ints vec, int a){
    ints idx;
    for(int i = 0; i < vec.size(); i++){
        if( vec[i] == a ) idx.emplace_back(i);
    }
    //int idx = std::find(vec.begin(), vec.end(), a) - vec.begin();
    return idx;
}

FourVectorVec gen4vec(floats &pt, floats &eta, floats &phi, floats &mass)
{
    FourVectorVec fourvecs;
    fourvecs.emplace_back(pt[0], eta[0], phi[0], mass[0]);
    return fourvecs;
}

template <typename T>
void plot(T hist, TString name){
  TCanvas * c = new TCanvas("c",Form("c_%s", name.Data()));
  hist->Write();
  hist->DrawClone();
  //c->Print(Form("hist_sig/%s.pdf",name.Data()));
  c->Print(Form("hist/%s.pdf",name.Data()));
  //c->Print(Form("%s.pdf",name.Data()));
}

floats LFVorigins( ints GenPart_pdgId, ints GenPart_genPartIdxMother,ints GenPart_status, ints GenPart_statusFlags, floats GenPart_pt, floats GenPart_eta, floats GenPart_phi, floats GenPart_mass ){
    floats out;
    //cout<<"###################"<<endl;
    int muon_idx=-1;
    int tau_idx=-1;
    ints b_idx;
    for( int i=0; i<GenPart_pdgId.size(); i++){
        int id = GenPart_pdgId[i];
        int m_idx = GenPart_genPartIdxMother[i];
        int m_id = GenPart_pdgId[m_idx];
        bool isLastMuon = abs(id) == 13 && GenPart_statusFlags[i] & 1 && !(GenPart_statusFlags[i] & 4);
        bool isLastTau = abs(id) == 15 && GenPart_statusFlags[i] & 1;
        bool isSMb = abs(id) == 5 && abs(m_id) == 6;
        if(isLastMuon){
            //cout<<"muon "<<bitset<15>(GenPart_statusFlags[i])<<endl;
            if(GenPart_statusFlags[i] & (1<<13)){
                muon_idx=i;
                //cout<<"isLastPrompt"<<endl;
            }
        }
        if(isLastTau){
            //cout<<"tau "<<bitset<15>(GenPart_statusFlags[i])<<endl;
            if(GenPart_statusFlags[i] & (1<<13)){
                tau_idx=i;
                //cout<<"isLastPrompt"<<endl;
            }
        }
        if(isSMb){
            //cout<<"SM b quark"<<endl;
            b_idx.emplace_back(i);
        }
    }
    if( muon_idx >= 0 && tau_idx >= 0 ){
        //cout<<"muon idx : "<<muon_idx<<endl;
        //cout<<"tau idx : "<<tau_idx<<endl;
        //cout<<"b idx : "<<b_idx<<endl;
    }
    out.emplace_back(muon_idx);
    out.emplace_back(tau_idx);
    for(int b_i:b_idx) out.emplace_back(b_i);
    //cout<<out<<endl;
    return out;
}

float deltaR(float eta1, float eta2, float phi1, float phi2){
    return DeltaR(eta1,eta2,phi1,phi2);
}

float invMass(float pt1, float eta1, float phi1, float mass1, float pt2, float eta2, float phi2, float mass2){
    TLorentzVector v1;
    TLorentzVector v2;
    v1.SetPtEtaPhiM(pt1,eta1,phi1,mass1);
    v2.SetPtEtaPhiM(pt2,eta2,phi2,mass2);
    return (v1+v2).M();
}
void ana_genLFV(const char * pname){
    std::string p="";
    if(strcmp(pname,"LFV_ST_TCMuTau_Scalar")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/ST_LFV_TCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_ST_TCMuTau_Vector")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/ST_LFV_TCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_ST_TCMuTau_Tensor")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/ST_LFV_TCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_ST_TUMuTau_Scalar")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/ST_LFV_TUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_ST_TUMuTau_Vector")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/ST_LFV_TUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_ST_TUMuTau_Tensor")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/ST_LFV_TUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_TT_TToCMuTau_Scalar")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/TT_LFV_TToCMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_TT_TToCMuTau_Vector")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/TT_LFV_TToCMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_TT_TToCMuTau_Tensor")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/TT_LFV_TToCMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_TT_TToUMuTau_Scalar")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/TT_LFV_TToUMuTau_Scalar_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_TT_TToUMuTau_Vector")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/TT_LFV_TToUMuTau_Vector_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"LFV_TT_TToUMuTau_Tensor")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL16NanoAODv2/TT_LFV_TToUMuTau_Tensor_TuneCP5_13TeV-madgraph-pythia8/NANOAODSIM/106X_mcRun2_asymptotic_v15-v2/270000/*.root";
    }else if(strcmp(pname,"SM_ttbar")==0){
        p="/data1/common/NanoAOD/v8_UL/mc/RunIISummer20UL18NanoAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v15_L1v1-v1/280000/*.root";
    }
    cout<<p<<endl;
    ROOT::RDataFrame df("Events",p);

    cout<<df.Count().GetValue()<<endl;

    auto df_genLFV = df.Define("LFVorigins",LFVorigins,{"GenPart_pdgId","GenPart_genPartIdxMother","GenPart_status","GenPart_statusFlags","GenPart_pt","GenPart_eta","GenPart_phi","GenPart_mass"})
                            .Define("muon_idx","LFVorigins[0]")
                            .Define("tau_idx","LFVorigins[1]")
                            .Define("b1_idx","LFVorigins[2]")
                            .Define("b2_idx","(int(LFVorigins.size())>3) ? LFVorigins[3] : -1")
                            .Filter("muon_idx > 0 && tau_idx > 0");
    auto df_genvar = df_genLFV.Define("mupt","GenPart_pt[muon_idx]")
                            .Define("mueta","GenPart_eta[muon_idx]")
                            .Define("muphi","GenPart_phi[muon_idx]")
                            .Define("mumass","GenPart_mass[muon_idx]")
                            .Define("taupt","GenPart_pt[tau_idx]")
                            .Define("taueta","GenPart_eta[tau_idx]")
                            .Define("tauphi","GenPart_phi[tau_idx]")
                            .Define("taumass","GenPart_mass[tau_idx]")
                            .Define("bpt","GenPart_pt[b1_idx]")
                            .Define("beta","GenPart_eta[b1_idx]")
                            .Define("bphi","GenPart_phi[b1_idx]")
                            .Define("bmass","GenPart_mass[b1_idx]")
                            .Define("lepdR",deltaR,{"mueta","taueta","muphi","tauphi"})
                            .Define("lepmass",invMass,{"mupt","mueta","muphi","mumass","taupt","taueta","tauphi","taumass"});

    //auto df_selevent = df_jet.Filter("ngoodgenjet > 0 && ngoodjet > 0","sel event");

    //auto disp = df_selevent.Display({"ngoodjet","ngoodgenjet","ngoodgenbjet","ngoodbjet","good_genjet_hadronFlavour","good_genjet_partonFlavour"},100);
    //auto disp = df_genvar.Display({"nJet","LFVorigins"},10);
    //disp->Print();
    auto h_mupt = df_genvar.Histo1D({"h_mupt","h_mupt",30,0,300},"mupt");
    auto h_taupt = df_genvar.Histo1D({"h_taupt","h_taupt",30,0,300},"taupt");
    auto h_bpt = df_genvar.Histo1D({"h_bpt","h_bpt",30,0,300},"bpt");
    auto h_mueta = df_genvar.Histo1D({"h_mueta","h_mueta",20,-4.0,4.0},"mueta");
    auto h_taueta = df_genvar.Histo1D({"h_taueta","h_taueta",20,-4.0,4.0},"taueta");
    auto h_beta = df_genvar.Histo1D({"h_beta","h_beta",20,-4.0,4.0},"beta");
    auto h_lepdR = df_genvar.Histo1D({"h_lepdR","h_mupt",12,0,6.0},"lepdR");
    auto h_lepmass = df_genvar.Histo1D({"h_lepmass","h_lepmass",20,0,400},"lepmass");
    
    TString name(pname);
    TFile f(Form("%s.root",name.Data()), "recreate");
    h_mupt->Write();
    h_taupt->Write();
    h_bpt->Write();
    h_mueta->Write();
    h_taueta->Write();
    h_beta->Write();
    h_lepdR->Write();
    h_lepmass->Write();
    f.Close();
}
