#include "ROOT/RDataFrame.hxx"
#include "ROOT/RVec.hxx"
#include "ROOT/RDF/RInterface.hxx"
#include "TCanvas.h"
#include "TH1D.h"
#include "TLatex.h"
#include "TLegend.h"
#include "Math/Vector4Dfwd.h"
#include "TStyle.h"

using namespace ROOT::VecOps;
using rvec_f = RVec<float>;

template <typename T>
void plot(T hist, TString name){
  TCanvas * c = new TCanvas("c",Form("c_%s", name.Data()));
  hist->DrawClone();
  c->Print(Form("%s.pdf",name.Data()));
}

void ana_lq(){

  //ROOT::RDataFrame df("Events", "/xrootd/store/data/Run2018B/SingleMuon/NANOAOD/Nano14Dec2018-v1/10000/BCC1B466-EF27-9D40-A0B7-9FE64F456E13.root");
  ROOT::RDataFrame df("Events", "signal_nano.root");

  auto df_S1_muon = df.Filter("nMuon >= 1", "Events with one lepton");
  auto df_S1_goodmuon = df_S1_muon.Filter("Sum( Muon_pt > 20  && abs(Muon_eta) < 2.4 && Muon_tightId && Muon_pfRelIso04_all < 0.15) >=1 ","Events with goood muon");

  auto h_n_muon = df_S1_goodmuon.Histo1D({"h_n_muon", "h_n_muon", 5, 0, 5}, "nMuon");
  auto h_n_tau = df_S1_goodmuon.Histo1D({"h_n_tau", "h_n_tau", 5, 0, 5}, "nTau");
  auto h_n_seltau = df_S1_goodmuon.Define("ntaujets", "Sum( Tau_idMVAoldDM > 1)").Histo1D({"h_n_seltau", "h_n_seltau", 5, 0, 5}, "ntaujets");
  auto h_n_cjets = df_S1_goodmuon.Define("ncjets","Sum( Jet_btagDeepC > 0.03 )").Histo1D({"h_n_cjets", "h_n_cjets", 5, 0, 5}, "ncjets");

  plot( h_n_muon, "h_n_muon");
  plot( h_n_tau, "h_n_tau");
  plot( h_n_seltau, "h_n_seltau");
  plot( h_n_cjets, "h_n_cjets");

  auto report = df_S1_goodmuon.Report();
  report->Print();

}
