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
  ROOT::RDataFrame df("Events", "signal_nano.root");

  //good muon selection
  auto df_S1_muon = df.Filter("nMuon >= 1", "Events with one lepton")
                      .Define("goodmuons","Muon_pt > 20  && abs(Muon_eta) < 2.4 && Muon_tightId && Muon_pfRelIso04_all < 0.15");
  auto df_S1_goodmuon = df_S1_muon.Filter("Sum( goodmuons ) >=1 ","Events with goood muon")
                                  .Define("goodmuons_idx",goodmuons_idx,{"goodmuons"})
                                  .Define("CvsB","Jet_btagDeepC/(Jet_btagDeepC+Jet_btagDeepB)");

  //histograms 
  auto h_muon_pt = df_S1_goodmuon.Define("muon_pt","Muon_pt[goodmuons][0]").Histo1D({"h_muon_pt", "h_muon_pt", 100, 0, 100}, "muon_pt");
  auto h_n_selmuon = df_S1_goodmuon.Define("n_selmuon","Sum(goodmuons)").Histo1D({"h_n_selmuon", "h_n_selmuon", 5, 0, 5}, "n_selmuon");
  auto h_n_tau = df_S1_goodmuon.Histo1D({"h_n_tau", "h_n_tau", 5, 0, 5}, "nTau");
  auto h_n_seltau = df_S1_goodmuon.Define("ntaujets", "Sum( Tau_idMVAoldDM > 1)").Histo1D({"h_n_seltau", "h_n_seltau", 5, 0, 5}, "ntaujets");
  auto h_ctag = df_S1_goodmuon.Histo1D({"h_ctag", "h_ctag", 100, 0, 1}, "CvsB");
  auto h_n_cjets = df_S1_goodmuon.Define("ncjets","Sum( CvsB > 0.33 )").Histo1D({"h_n_cjets", "h_n_cjets", 5, 0, 5}, "ncjets");
  auto h_n_bjets_l = df_S1_goodmuon.Define("nbjets_l","Sum( Jet_btagDeepB > 0.0521 )").Histo1D({"h_n_bjets_l", "h_n_bjets_l", 5, 0, 5}, "nbjets_l");
  auto h_n_bjets_m = df_S1_goodmuon.Define("nbjets_m","Sum( Jet_btagDeepB > 0.3033 )").Histo1D({"h_n_bjets_m", "h_n_bjets_m", 5, 0, 5}, "nbjets_m");
  auto h_n_bjets_t = df_S1_goodmuon.Define("nbjets_t","Sum( Jet_btagDeepB > 0.7489 )").Histo1D({"h_n_bjets_t", "h_n_bjets_t", 5, 0, 5}, "nbjets_t");
                              

  plot( h_muon_pt, "h_muon_pt");
  plot( h_n_selmuon, "h_n_selmuon");
  plot( h_n_tau, "h_n_tau");
  plot( h_n_seltau, "h_n_seltau");
  plot( h_ctag, "h_ctag");
  plot( h_n_cjets, "h_n_cjets");
  plot( h_n_bjets_l, "h_n_bjets_l");
  plot( h_n_bjets_m, "h_n_bjets_m");
  plot( h_n_bjets_t, "h_n_bjets_t");

  auto report = df_S1_goodmuon.Report();
  report->Print();

}
