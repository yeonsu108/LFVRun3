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

using namespace ROOT::VecOps;
using rvec_f = RVec<float>;
using rvec_b = RVec<bool>;
using rvec_i = RVec<int>;

template <typename T>
void plot(T hist, TString name){
  TCanvas * c = new TCanvas("c",Form("c_%s", name.Data()));
  hist->Write();
  hist->DrawClone();
  c->Print(Form("%s.pdf",name.Data()));
}

vector<int> goodmuons_idx(rvec_i g){
  vector<int> out;
  for(int i = 0; i < g.size(); i++){
    if( g[i] ) out.push_back( i );
  }
  return out; 
}

void ana_lq(){

  //ROOT::RDataFrame df("Events", "/xrootd/store/data/Run2018B/SingleMuon/NANOAOD/Nano14Dec2018-v1/10000/BCC1B466-EF27-9D40-A0B7-9FE64F456E13.root");
  //ROOT::RDataFrame df("Events", "signal_nano.root");
  ROOT::RDataFrame df("Events", "/xrootd/store/user/ljw1015/LQ_Signals/LQ_2017_nano_v1.root");
  //ROOT::RDataFrame df("Events","/xrootd/store/mc/RunIISummer16NanoAODv6/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/NANOAODSIM/PUMoriond17_Nano25Oct2019_102X_mcRun2_asymptotic_v7-v2/30000/A7753E9B-A80C-9547-8729-17F953C5B5DE.root");
  //ROOT::RDataFrame df("Events", "/xrootd/store/user/ljw1015/LQ_Signals/LQ_2016_nano.root");

  //good muon selection
  auto df_S1_muon = df.Filter("nMuon >= 1", "Events with one lepton")
                      .Define("goodmuons","Muon_pt > 20  && abs(Muon_eta) < 2.4 && Muon_tightId && Muon_pfRelIso04_all < 0.15")
                      .Define("goodtaus","Tau_pt > 30 && abs(Tau_eta) < 2.4 && Sum( Tau_idMVAoldDM > 1)");
  auto df_S1_goodmuon = df_S1_muon.Filter("Sum( goodmuons ) >=1 ","Events with at least a goood muon")
                                  .Define("goodmuons_idx",goodmuons_idx,{"goodmuons"});
  auto df_S1_goodtau = df_S1_goodmuon.Filter("Sum( goodtaus ) >=1 ","Events with at least a goood tau")
                                     .Define("CvsB","Jet_btagDeepC/(Jet_btagDeepC+Jet_btagDeepB)")
                                     .Define("goodcjets","Jet_pt > 20 && abs(Jet_eta) < 2.4 && CvsB > 0.33")
                                     .Define("goodbjets_l","Jet_pt > 20 && abs(Jet_eta) < 2.4 && Jet_btagDeepB > 0.0521")
                                     .Define("goodbjets_m","Jet_pt > 20 && abs(Jet_eta) < 2.4 && Jet_btagDeepB > 0.3033")
                                     .Define("goodbjets_t","Jet_pt > 20 && abs(Jet_eta) < 2.4 && Jet_btagDeepB > 0.7489");
  auto df_S1_bjets = df_S1_goodtau.Filter("Sum( goodbjets_m ) >=1","Events with at least a b jet");
  auto df_S1_ttb = df_S1_bjets.Filter("(genTtbarId/10)%10 == 5","ttb+bb event");

  //histograms 
  auto h_muon_pt = df_S1_goodmuon.Define("muon_pt","Muon_pt[goodmuons][0]").Histo1D({"h_muon_pt", "h_muon_pt", 100, 0, 100}, "muon_pt");
  auto h_n_selmuon = df_S1_goodmuon.Define("n_selmuon","Sum(goodmuons)").Histo1D({"h_n_selmuon", "h_n_selmuon", 5, 0, 5}, "n_selmuon");
  auto h_n_tau = df_S1_goodmuon.Histo1D({"h_n_tau", "h_n_tau", 5, 0, 5}, "nTau");
  auto h_n_seltau = df_S1_goodmuon.Define("ntaujets", "Sum(goodtaus)").Histo1D({"h_n_seltau", "h_n_seltau", 5, 0, 5}, "ntaujets");
  auto h_ctag = df_S1_goodtau.Histo1D({"h_ctag", "h_ctag", 100, 0, 1}, "CvsB");
  auto h_n_cjets = df_S1_goodtau.Define("ncjets","Sum( goodcjets )").Histo1D({"h_n_cjets", "h_n_cjets", 5, 0, 5}, "ncjets");
  auto h_n_bjets_l = df_S1_goodtau.Define("nbjets_l","Sum( goodbjets_l )").Histo1D({"h_n_bjets_l", "h_n_bjets_l", 5, 0, 5}, "nbjets_l");
  auto h_n_bjets_m = df_S1_goodtau.Define("nbjets_m","Sum( goodbjets_m )").Histo1D({"h_n_bjets_m", "h_n_bjets_m", 5, 0, 5}, "nbjets_m");
  auto h_n_bjets_t = df_S1_goodtau.Define("nbjets_t","Sum( goodbjets_t )").Histo1D({"h_n_bjets_t", "h_n_bjets_t", 5, 0, 5}, "nbjets_t");
                              
  //df_S1_goodmuon.Snapshot("tree", "f.root");
  TFile f("f.root", "recreate");

  plot( h_muon_pt, "h_muon_pt");
  plot( h_n_selmuon, "h_n_selmuon");
  plot( h_n_tau, "h_n_tau");
  plot( h_n_seltau, "h_n_seltau");
  plot( h_ctag, "h_ctag");
  plot( h_n_cjets, "h_n_cjets");
  plot( h_n_bjets_l, "h_n_bjets_l");
  plot( h_n_bjets_m, "h_n_bjets_m");
  plot( h_n_bjets_t, "h_n_bjets_t");

  f.Close();

  auto report = df_S1_bjets.Report();
  report->Print();

}
