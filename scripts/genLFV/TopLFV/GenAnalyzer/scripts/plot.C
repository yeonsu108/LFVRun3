#include "tdrstyle.C"
/*
void make2Plot(TFile * f, TString title, TString name1, TString name2, TString ytitle, TString xtitle, float x1, float y1, float x2, float y2){

  TH1F * h1 = (TH1F*) f->Get(Form("genana/%s", name1.Data()));
  TH1F * h2 = (TH1F*) f->Get(Form("genana/%s", name2.Data()));

  cout<<h1<<endl;
  cout<<h2<<endl;
  TCanvas * c = new TCanvas(Form("c_%s",title.Data()),"c",1);
  h1->Sumw2();
  h2->Sumw2();
  h1->Scale(1.0/h1->Integral());
  h2->Scale(1.0/h2->Integral());
  h1->SetLineWidth(2);
  h2->SetLineWidth(2);
  h1->SetLineColor(kRed);
  h2->SetLineColor(kBlue);
  h2->SetStats(0);
  h2->SetTitle("");
  double max_h1 = h1->GetMaximum();
  double max_h2 = h2->GetMaximum();
  double max = std::max(max_h1,max_h2);
  h1->SetMaximum(max*1.2);
  h1->Draw("E");
  h1->Draw("SameHIST");
  h1->GetXaxis()->SetTitle(Form("%s",xtitle.Data()));
  h1->GetYaxis()->SetTitle(Form("%s",ytitle.Data()));
  h2->Draw("SameE");
  h2->Draw("SameHIST");

  TLegend * l = new TLegend(x1,y1,x2,y2);
  l->AddEntry(h1,Form("%s", name1.Data()),"L");
  l->AddEntry(h2,Form("%s", name2.Data()),"L");
  l->SetTextSize(0.04);
  l->SetFillColor(0);
  l->SetLineColor(0);
  l->Draw();

  c->Print(Form("genana_plots_v3/%s.pdf",title.Data()));

}

void make3Plot(TFile * f, TString title, TString name1, TString name2, TString name3, TString ytitle, TString xtitle, float x1, float y1, float x2, float y2){

  TH1F * h1 = (TH1F*) f->Get(Form("%s", name1.Data()));
  TH1F * h2 = (TH1F*) f->Get(Form("%s", name2.Data()));
  TH1F * h3 = (TH1F*) f->Get(Form("%s", name3.Data()));

  TCanvas * c = new TCanvas(Form("c_%s",title.Data()),"c",1);
  h1->Sumw2();
  h2->Sumw2();
  h3->Sumw2();
  h1->Scale(1.0/h1->Integral());
  h2->Scale(1.0/h2->Integral());
  h3->Scale(1.0/h3->Integral());
  h1->SetLineWidth(2);
  h2->SetLineWidth(2);
  h3->SetLineWidth(2);
  h1->SetLineColor(kRed);
  h2->SetLineColor(kBlue);
  h3->SetLineColor(kViolet);
  h2->SetStats(0);
  h2->SetTitle("");
  double max_h1 = h1->GetMaximum();
  double max_h2 = h2->GetMaximum();
  double max_h3 = h3->GetMaximum();
  double max = std::max(std::max(max_h1,max_h2), max_h3);
  //double max = std::max(max_h1,max_h2);
  h1->SetMaximum(max*1.2);
  h1->Draw("E");
  h1->Draw("SameHIST");
  h1->GetXaxis()->SetTitle(Form("%s",xtitle.Data()));
  h1->GetYaxis()->SetTitle(Form("%s",ytitle.Data()));
  h2->Draw("SameE");
  h2->Draw("SameHIST");
  h3->Draw("SameE");
  h3->Draw("SameHIST");

  TLegend * l = new TLegend(x1,y1,x2,y2);
  //l->AddEntry(h1,"Jet associated with tau","L");
  //l->AddEntry(h2,"Jet not associated with tau","L");
  //l->AddEntry(h3,"Tau has no associated jet","L");
  l->AddEntry(h1,"c quark from top","L");
  l->AddEntry(h2,"c quark from W","L");
  l->AddEntry(h3,"c quark from gluon","L");
  l->SetTextSize(0.04);
  l->SetFillColor(0);
  l->SetLineColor(0);
  l->Draw();

  c->Print(Form("%s.pdf",title.Data()));

}

void make4Plot(TFile * f, TString title, TString name1, TString name2, TString name3, TString name4, TString ytitle, TString xtitle, float x1, float y1, float x2, float y2){

  TH1F * h1 = (TH1F*) f->Get(Form("%s", name1.Data()));
  TH1F * h2 = (TH1F*) f->Get(Form("%s", name2.Data()));
  TH1F * h3 = (TH1F*) f->Get(Form("%s", name3.Data()));
  TH1F * h4 = (TH1F*) f->Get(Form("%s", name4.Data()));

  TCanvas * c = new TCanvas(Form("c_%s",title.Data()),"c",1);
  h1->Sumw2();
  h2->Sumw2();
  h3->Sumw2();
  h4->Sumw2();
  h1->Scale(1.0/h1->Integral());
  h2->Scale(1.0/h2->Integral());
  h3->Scale(1.0/h3->Integral());
  h4->Scale(1.0/h4->Integral());
  h1->SetLineWidth(2);
  h2->SetLineWidth(2);
  h3->SetLineWidth(2);
  h4->SetLineWidth(2);
  h1->SetLineColor(kRed);
  h2->SetLineColor(kBlue);
  h3->SetLineColor(kViolet);
  h4->SetLineColor(kGreen);
  h2->SetStats(0);
  h2->SetTitle("");
  double max_h1 = h1->GetMaximum();
  double max_h2 = h2->GetMaximum();
  double max_h3 = h3->GetMaximum();
  double max_h4 = h4->GetMaximum();
  double max = std::max(std::max(std::max(max_h1,max_h2),max_h3),max_h4);
  //double max = std::max(max_h1,max_h2);
  h1->SetMaximum(max*1.2);
  h1->Draw("E");
  h1->Draw("HIST");
  h2->Draw("SameE");
  h2->Draw("SameHIST");
  h3->Draw("SameE");
  h3->Draw("SameHIST");
  h4->Draw("SameE");
  h4->Draw("SameHIST");
  h1->GetXaxis()->SetTitle(Form("%s",xtitle.Data()));
  h1->GetYaxis()->SetTitle(Form("%s",ytitle.Data()));

  TLegend * l = new TLegend(x1,y1,x2,y2);
  l->AddEntry(h1,Form("%s", name1.Data()),"L");
  l->AddEntry(h2,Form("%s", name2.Data()),"L");
  l->AddEntry(h3,Form("%s", name3.Data()),"L");
  l->AddEntry(h4,Form("%s", name4.Data()),"L");
  l->SetTextSize(0.04);
  l->SetFillColor(0);
  l->SetLineColor(0);
  l->Draw();

  c->Print(Form("%s.pdf",title.Data()));

}

void make6filePlot(TFile * f1, TFile * f2,TFile * f3,TFile * f4,TFile * f5, TFile * f6, TString name, TString ytitle, TString xtitle, float x1, float y1, float x2, float y2){

  TH1F * h1 = (TH1F*) f1->Get(Form("genana/%s", name.Data()));
  TH1F * h2 = (TH1F*) f2->Get(Form("genana/%s", name.Data()));
  TH1F * h3 = (TH1F*) f3->Get(Form("genana/%s", name.Data()));
  TH1F * h4 = (TH1F*) f4->Get(Form("genana/%s", name.Data()));
  TH1F * h5 = (TH1F*) f5->Get(Form("genana/%s", name.Data()));
  TH1F * h6 = (TH1F*) f6->Get(Form("genana/%s", name.Data()));

  cout<<h1<<endl;
  cout<<h2<<endl;
  cout<<h3<<endl;
  cout<<h4<<endl;
  cout<<h5<<endl;
  cout<<h6<<endl;
  TCanvas * c = new TCanvas(Form("c_%s",name.Data()),"c",1);
  h1->Sumw2();
  h2->Sumw2();
  h3->Sumw2();
  h4->Sumw2();
  h5->Sumw2();
  h6->Sumw2();
  h1->Scale(1.0/h1->Integral());
  h2->Scale(1.0/h2->Integral());
  h3->Scale(1.0/h3->Integral());
  h4->Scale(1.0/h4->Integral());
  h5->Scale(1.0/h5->Integral());
  h6->Scale(1.0/h6->Integral());
  h1->SetLineWidth(2);
  h2->SetLineWidth(2);
  h3->SetLineWidth(2);
  h4->SetLineWidth(2);
  h5->SetLineWidth(2);
  h6->SetLineWidth(2);
  h1->SetLineColor(kRed);
  h2->SetLineColor(kGreen);
  h3->SetLineColor(kBlue);
  h4->SetLineColor(kYellow);
  h5->SetLineColor(kMagenta);
  h6->SetLineColor(kCyan);
  h1->SetStats(0);
  h1->SetTitle("");
  double max_h1 = h1->GetMaximum();
  double max_h2 = h2->GetMaximum();
  double max_h3 = h3->GetMaximum();
  double max_h4 = h4->GetMaximum();
  double max_h5 = h5->GetMaximum();
  double max_h6 = h6->GetMaximum();
  double max = std::max(std::max(std::max(std::max(std::max(max_h1,max_h2),max_h3),max_h4),max_h5),max_h6);
  //double max = std::max(max_h1,max_h2);
  h1->SetMaximum(max*1.2);
//  h1->Draw("E");
  h1->Draw("HIST");
//  h2->Draw("SameE");
  h2->Draw("SameHIST");
//  h3->Draw("SameE");
  h3->Draw("SameHIST");
//  h4->Draw("SameE");
  h4->Draw("SameHIST");
//  h5->Draw("SameE");
  h5->Draw("SameHIST");
//  h6->Draw("SameE");
  h6->Draw("SameHIST");
  h1->GetXaxis()->SetTitle(Form("%s",xtitle.Data()));
  h1->GetXaxis()->SetTitleSize(0.05);
  h1->GetYaxis()->SetTitle(Form("%s",ytitle.Data()));
  h1->GetYaxis()->SetTitleSize(0.05);

  TLegend * l = new TLegend(x1,y1,x2,y2);
  l->AddEntry(h1,"Clq","L");
  l->AddEntry(h2,"Clu","L");
  l->AddEntry(h3,"Cqe","L");
  l->AddEntry(h4,"Ceu","L");
  l->AddEntry(h5,"Clequ1","L");
  l->AddEntry(h6,"Clequ3","L");
  l->SetTextSize(0.04);
  l->SetFillColor(0);
  l->SetLineColor(0);
  l->Draw();

  c->Print(Form("genana_plots_v2/%s.pdf",name.Data()));

}
void make7filePlot(TFile * f1, TFile * f2,TFile * f3,TFile * f4,TFile * f5, TFile * f6, TFile * f7, TString name, TString ytitle, TString xtitle, float x1, float y1, float x2, float y2){

  TH1F * h1 = (TH1F*) f1->Get(Form("genana/%s", name.Data()));
  TH1F * h2 = (TH1F*) f2->Get(Form("genana/%s", name.Data()));
  TH1F * h3 = (TH1F*) f3->Get(Form("genana/%s", name.Data()));
  TH1F * h4 = (TH1F*) f4->Get(Form("genana/%s", name.Data()));
  TH1F * h5 = (TH1F*) f5->Get(Form("genana/%s", name.Data()));
  TH1F * h6 = (TH1F*) f6->Get(Form("genana/%s", name.Data()));
  TH1F * h7 = (TH1F*) f7->Get(Form("genana/%s", name.Data()));

  cout<<h1<<endl;
  cout<<h2<<endl;
  cout<<h3<<endl;
  cout<<h4<<endl;
  cout<<h5<<endl;
  cout<<h6<<endl;
  cout<<h7<<endl;
  
  TCanvas * c = new TCanvas(Form("c_%s",name.Data()),"c",1);
   
  h1->Sumw2();
  h2->Sumw2();
  h3->Sumw2();
  h4->Sumw2();
  h5->Sumw2();
  h6->Sumw2();
  h7->Sumw2();
  h1->Scale(1.0/h1->Integral());
  h2->Scale(1.0/h2->Integral());
  h3->Scale(1.0/h3->Integral());
  h4->Scale(1.0/h4->Integral());
  h5->Scale(1.0/h5->Integral());
  h6->Scale(1.0/h6->Integral());
  h7->Scale(1.0/h7->Integral());
  h1->SetLineWidth(2);
  h2->SetLineWidth(2);
  h3->SetLineWidth(2);
  h4->SetLineWidth(2);
  h5->SetLineWidth(2);
  h6->SetLineWidth(2);
  h7->SetLineWidth(2);
  h1->SetLineColor(kCyan);
  h2->SetLineColor(kCyan+1);
  h3->SetLineColor(kCyan+2);
  h4->SetLineColor(kCyan+3);
  h5->SetLineColor(kGreen+1);
  h6->SetLineColor(kRed+1);
  h7->SetLineColor(kMagenta+1);
//  h1->SetLineColor(kRed);
//  h2->SetLineColor(kGreen);
//  h3->SetLineColor(kBlue);
//  h4->SetLineColor(kYellow);
//  h5->SetLineColor(kMagenta);
//  h6->SetLineColor(kCyan);
//  h7->SetLineColor(kBlack);
  h1->SetStats(0);
  h1->SetTitle("");
  double max_h1 = h1->GetMaximum();
  double max_h2 = h2->GetMaximum();
  double max_h3 = h3->GetMaximum();
  double max_h4 = h4->GetMaximum();
  double max_h5 = h5->GetMaximum();
  double max_h6 = h6->GetMaximum();
  double max_h7 = h7->GetMaximum();
  double max = std::max(std::max(std::max(std::max(std::max(std::max(max_h1,max_h2),max_h3),max_h4),max_h5),max_h6),max_h7);
  //double max = std::max(max_h1,max_h2);
  h7->SetMaximum(max*1.2);
//  h1->Draw("E");
  h7->Draw("HIST");
  h1->Draw("SameHIST");
//  h2->Draw("SameE");
  h2->Draw("SameHIST");
//  h3->Draw("SameE");
  h3->Draw("SameHIST");
//  h4->Draw("SameE");
  h4->Draw("SameHIST");
//  h5->Draw("SameE");
  h5->Draw("SameHIST");
//  h6->Draw("SameE");
  h6->Draw("SameHIST");
  h7->GetXaxis()->SetTitle(Form("%s",xtitle.Data()));
  h7->GetXaxis()->SetTitleSize(0.05);
  h7->GetYaxis()->SetTitle(Form("%s",ytitle.Data()));
  h7->GetYaxis()->SetTitleSize(0.05);
  

  TLegend * l = new TLegend(x1,y1,x2,y2);
  l->AddEntry(h1,"Clq","L");
  l->AddEntry(h2,"Clu","L");
  l->AddEntry(h3,"Cqe","L");
  l->AddEntry(h4,"Ceu","L");
  l->AddEntry(h5,"Clequ1","L");
  l->AddEntry(h6,"Clequ3","L");
  l->AddEntry(h7,"LQ","L");
  l->SetTextSize(0.04);
  l->SetFillColor(0);
  l->SetLineColor(0);
  l->Draw();

  float xmin = h7->GetXaxis()->GetXmin();
  float xmax = h7->GetXaxis()->GetXmax();
  float xrange = xmax - xmin;
  
  TLatex latex;
  latex.SetTextAlign(11); 
  latex.SetTextSize(0.04);
  latex.DrawLatex(xmin + xrange * 0.05, max*1.2*0.9, "CMS Simulation");

  c->Print(Form("genana_plots_v1/%s.pdf",name.Data()));

}

void make4LFVfilePlot(TFile * f1, TFile * f2,TFile * f3,TFile * f4, TString name, TString ytitle, TString xtitle, float x1, float y1, float x2, float y2){

  TH1F * h1 = (TH1F*) f1->Get(Form("genana/%s", name.Data()));
  TH1F * h2 = (TH1F*) f2->Get(Form("genana/%s", name.Data()));
  TH1F * h3 = (TH1F*) f3->Get(Form("genana/%s", name.Data()));
  TH1F * h4 = (TH1F*) f4->Get(Form("genana/%s", name.Data()));

  cout<<h1<<endl;
  cout<<h2<<endl;
  cout<<h3<<endl;
  cout<<h4<<endl;
  
  TCanvas * c = new TCanvas(Form("c_%s",name.Data()),"c",1);
   
  h1->Sumw2();
  h2->Sumw2();
  h3->Sumw2();
  h4->Sumw2();
  h1->Scale(1.0/h1->Integral());
  h2->Scale(1.0/h2->Integral());
  h3->Scale(1.0/h3->Integral());
  h4->Scale(1.0/h4->Integral());
  h1->SetLineWidth(2);
  h2->SetLineWidth(2);
  h3->SetLineWidth(2);
  h4->SetLineWidth(2);
  h1->SetLineColor(kGreen+1);
  h2->SetLineColor(kCyan+2);
  h3->SetLineColor(kRed+1);
  h4->SetLineColor(kMagenta+1);
  h1->SetStats(0);
  h1->SetTitle("");
  double max_h1 = h1->GetMaximum();
  double max_h2 = h2->GetMaximum();
  double max_h3 = h3->GetMaximum();
  double max_h4 = h4->GetMaximum();
  double max = std::max(std::max(std::max(max_h1,max_h2),max_h3),max_h4);
  //double max = std::max(max_h1,max_h2);
  h1->SetMaximum(max*1.2);
//  h1->Draw("E");
  h1->Draw("HIST");
  h2->Draw("SameHIST");
  h3->Draw("SameHIST");
  h4->Draw("SameHIST");
  h1->GetXaxis()->SetTitle(Form("%s",xtitle.Data()));
  h1->GetXaxis()->SetTitleSize(0.05);
  h1->GetYaxis()->SetTitle(Form("%s",ytitle.Data()));
  h1->GetYaxis()->SetTitleSize(0.05);
  

  TLegend * l = new TLegend(x1,y1,x2,y2);
  l->AddEntry(h1,"Scalar","L");
  l->AddEntry(h2,"Vector","L");
  l->AddEntry(h3,"Tensor","L");
  l->AddEntry(h4,"LQ","L");
  l->SetTextSize(0.04);
  l->SetFillColor(0);
  l->SetLineColor(0);
  l->Draw();

  float xmin = h1->GetXaxis()->GetXmin();
  float xmax = h1->GetXaxis()->GetXmax();
  float xrange = xmax - xmin;
  
  TLatex latex;
  latex.SetTextAlign(11); 
  latex.SetTextSize(0.04);
  latex.DrawLatex(xmin + xrange * 0.05, max*1.2*0.9, "CMS Simulation");

  c->Print(Form("genana_plots_v1/merged_%s.pdf",name.Data()));

}
*/
void make3LFVfilePlot(TFile * f1, TFile * f2,TFile * f3, TString name, TString fname, TString ytitle, TString xtitle, float x1, float y1, float x2, float y2){

  TH1D * h1 = (TH1D*) f1->Get(Form("genana/%s", name.Data()));
  TH1D * h2 = (TH1D*) f2->Get(Form("genana/%s", name.Data()));
  TH1D * h3 = (TH1D*) f3->Get(Form("genana/%s", name.Data()));

  cout<<h1<<endl;
  cout<<h2<<endl;
  cout<<h3<<endl;
  
  TCanvas * c = new TCanvas(Form("c_%s",name.Data()),"c",1);
   
  h1->Sumw2();
  h2->Sumw2();
  h3->Sumw2();
  h1->Scale(1.0/h1->Integral());
  h2->Scale(1.0/h2->Integral());
  h3->Scale(1.0/h3->Integral());
  h1->SetLineWidth(2);
  h2->SetLineWidth(2);
  h3->SetLineWidth(2);
  h1->SetLineColor(kGreen+1);
  h2->SetLineColor(kCyan+2);
  h3->SetLineColor(kRed+1);
  h1->SetStats(0);
  h1->SetTitle("");
  double max_h1 = h1->GetMaximum();
  double max_h2 = h2->GetMaximum();
  double max_h3 = h3->GetMaximum();
  double max = std::max(std::max(max_h1,max_h2),max_h3);
  //double max = std::max(max_h1,max_h2);
  h1->SetMaximum(max*1.2);
//  h1->Draw("E");
  h1->Draw("HIST");
  h2->Draw("SameHIST");
  h3->Draw("SameHIST");
  h1->GetXaxis()->SetTitle(Form("%s",xtitle.Data()));
  h1->GetXaxis()->SetTitleSize(0.05);
  h1->GetYaxis()->SetTitle(Form("%s",ytitle.Data()));
  h1->GetYaxis()->SetTitleSize(0.05);
  

  TLegend * l = new TLegend(x1,y1,x2,y2);
  l->AddEntry(h1,"Scalar","L");
  l->AddEntry(h2,"Vector","L");
  l->AddEntry(h3,"Tensor","L");
  l->SetTextSize(0.045);
  l->SetFillColor(0);
  l->SetLineColor(0);
  l->Draw();

  float xmin = h1->GetXaxis()->GetXmin();
  float xmax = h1->GetXaxis()->GetXmax();
  float xrange = xmax - xmin;
  
  TLatex latex;
  latex.SetTextAlign(11); 
  latex.SetTextSize(0.04);
  latex.DrawLatex(xmin + xrange * 0.05, max*1.2*0.9, "CMS Simulation");

  c->Print(Form("may_LFV/%s_%s.pdf",name.Data(),fname.Data()));

}
void make5LFVfilePlot(TFile * f, TFile * f1, TFile * f2,TFile * f3,TFile * f4, TString name, TString ytitle, TString xtitle, float x1, float y1, float x2, float y2){

  TH1D * h = (TH1D*) f->Get(Form("genana/%s", name.Data()));
  TH1D * h1 = (TH1D*) f1->Get(Form("genana/%s", name.Data()));
  TH1D * h2 = (TH1D*) f2->Get(Form("genana/%s", name.Data()));
  TH1D * h3 = (TH1D*) f3->Get(Form("genana/%s", name.Data()));
  TH1D * h4 = (TH1D*) f4->Get(Form("genana/%s", name.Data()));

  cout<<h<<endl;
  cout<<h1<<endl;
  cout<<h2<<endl;
  cout<<h3<<endl;
  cout<<h4<<endl;
  
  TCanvas * c = new TCanvas(Form("c_%s",name.Data()),"c",1);
   
  h->Sumw2();
  h1->Sumw2();
  h2->Sumw2();
  h3->Sumw2();
  h4->Sumw2();
  h->Scale(1.0/h->Integral());
  h1->Scale(1.0/h1->Integral());
  h2->Scale(1.0/h2->Integral());
  h3->Scale(1.0/h3->Integral());
  h4->Scale(1.0/h4->Integral());
  h->SetLineWidth(2);
  h1->SetLineWidth(2);
  h2->SetLineWidth(2);
  h3->SetLineWidth(2);
  h4->SetLineWidth(2);
  h->SetLineColor(kBlack);
  h1->SetLineColor(kGreen+1);
  h2->SetLineColor(kCyan+2);
  h3->SetLineColor(kRed+1);
  h4->SetLineColor(kMagenta+1);
  h->SetStats(0);
  h->SetTitle("");
  double max_h = h->GetMaximum();
  double max_h1 = h1->GetMaximum();
  double max_h2 = h2->GetMaximum();
  double max_h3 = h3->GetMaximum();
  double max_h4 = h4->GetMaximum();
  double max = std::max(std::max(std::max(std::max(max_h,max_h1),max_h2),max_h3),max_h4);
  //double max = std::max(max_h1,max_h2);
  h->SetMaximum(max*1.2);
//  h1->Draw("E");
  h->Draw("HIST");
  h1->Draw("SameHIST");
  h2->Draw("SameHIST");
  h3->Draw("SameHIST");
  h4->Draw("SameHIST");
  h->GetXaxis()->SetTitle(Form("%s",xtitle.Data()));
  h->GetXaxis()->SetTitleSize(0.05);
  h->GetYaxis()->SetTitle(Form("%s",ytitle.Data()));
  h->GetYaxis()->SetTitleSize(0.05);
  

  TLegend * l = new TLegend(x1,y1,x2,y2);
  l->AddEntry(h,"SM #it{t#bar{t}}","L");
  l->AddEntry(h1,"ST #it{tc#mu#tau}","L");
  l->AddEntry(h2,"ST #it{tu#mu#tau}","L");
  l->AddEntry(h3,"TT #it{tc#mu#tau}","L");
  l->AddEntry(h4,"TT #it{tu#mu#tau}","L");
  l->SetTextSize(0.045);
  l->SetFillColor(0);
  l->SetLineColor(0);
  l->Draw();

  float xmin = h->GetXaxis()->GetXmin();
  float xmax = h->GetXaxis()->GetXmax();
  float xrange = xmax - xmin;
  
  TLatex latex;
  latex.SetTextAlign(11); 
  latex.SetTextSize(0.04);
  latex.DrawLatex(xmin + xrange * 0.05, max*1.2*0.9, "CMS Simulation");

  c->Print(Form("may_LFV/%s_tensor.pdf",name.Data()));

}
void plot(){

  setTDRStyle();

  //TFile * f = new TFile("ttsemi_taujet.root");
  //TFile * f = new TFile("out_findmother.root");

  TFile * f = new TFile("may_LFV/SM_TTbar_dileptonic_V1.root");

  TFile * f11 = new TFile("may_LFV/LFV_ST_TCMuTau_Scalar_V1.root");
  TFile * f12 = new TFile("may_LFV/LFV_ST_TUMuTau_Scalar_V1.root");
  TFile * f13 = new TFile("may_LFV/LFV_TT_TCMuTau_Scalar_V1.root");
  TFile * f14 = new TFile("may_LFV/LFV_TT_TUMuTau_Scalar_V1.root");

  TFile * f21 = new TFile("may_LFV/LFV_ST_TCMuTau_Vector_V1.root");
  TFile * f22 = new TFile("may_LFV/LFV_ST_TUMuTau_Vector_V1.root");
  TFile * f23 = new TFile("may_LFV/LFV_TT_TCMuTau_Vector_V1.root");
  TFile * f24 = new TFile("may_LFV/LFV_TT_TUMuTau_Vector_V1.root");

  TFile * f31 = new TFile("may_LFV/LFV_ST_TCMuTau_Tensor_V1.root");
  TFile * f32 = new TFile("may_LFV/LFV_ST_TUMuTau_Tensor_V1.root");
  TFile * f33 = new TFile("may_LFV/LFV_TT_TCMuTau_Tensor_V1.root");
  TFile * f34 = new TFile("may_LFV/LFV_TT_TUMuTau_Tensor_V1.root");

//  make5LFVfilePlot(f,f1,f2,f3,f4,"lepdR","Normalized Entries","#Delta R(#mu,#tau)", 0.70, 0.65, 0.85, 0.9);
//  make5LFVfilePlot(f,f1,f2,f3,f4,"lepmass","Normalized Entries","M(#mu,#tau)", 0.70, 0.65, 0.85, 0.9);
//  make5LFVfilePlot(f,f1,f2,f3,f4,"bpt","Normalized Entries","p_{T}_{b}", 0.70, 0.65, 0.85, 0.9);
//  make5LFVfilePlot(f,f1,f2,f3,f4,"mupt","Normalized Entries","p_{T}_{#mu}", 0.70, 0.65, 0.85, 0.9);
//  make5LFVfilePlot(f,f1,f2,f3,f4,"taupt","Normalized Entries","p_{T}_{#tau}", 0.70, 0.65, 0.85, 0.9);
//  make5LFVfilePlot(f,f1,f2,f3,f4,"beta","Normalized Entries","|#eta|_{b}", 0.70, 0.65, 0.85, 0.9);
//  make5LFVfilePlot(f,f1,f2,f3,f4,"mueta","Normalized Entries","|#eta|_{#mu}", 0.70, 0.65, 0.85, 0.9);
//  make5LFVfilePlot(f,f1,f2,f3,f4,"taueta","Normalized Entries","|#eta|_{#tau}", 0.70, 0.65, 0.85, 0.9); 
  
  make3LFVfilePlot(f11,f21,f31,"lepdR","LFV_ST_TCMuTau","Normalized Entries","#Delta R(#mu,#tau)", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f11,f21,f31,"lepmass","LFV_ST_TCMuTau","Normalized Entries","M(#mu,#tau)", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f11,f21,f31,"bpt","LFV_ST_TCMuTau","Normalized Entries","p_{T}_{b}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f11,f21,f31,"mupt","LFV_ST_TCMuTau","Normalized Entries","p_{T}_{#mu}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f11,f21,f31,"taupt","LFV_ST_TCMuTau","Normalized Entries","p_{T}_{#tau}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f11,f21,f31,"beta","LFV_ST_TCMuTau","Normalized Entries","|#eta|_{b}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f11,f21,f31,"mueta","LFV_ST_TCMuTau","Normalized Entries","|#eta|_{#mu}", 0.70, 0.65, 0.85, 0.9);
  
  make3LFVfilePlot(f12,f22,f32,"lepdR","LFV_ST_TUMuTau","Normalized Entries","#Delta R(#mu,#tau)", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f12,f22,f32,"lepmass","LFV_ST_TUMuTau","Normalized Entries","M(#mu,#tau)", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f12,f22,f32,"bpt","LFV_ST_TUMuTau","Normalized Entries","p_{T}_{b}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f12,f22,f32,"mupt","LFV_ST_TUMuTau","Normalized Entries","p_{T}_{#mu}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f12,f22,f32,"taupt","LFV_ST_TUMuTau","Normalized Entries","p_{T}_{#tau}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f12,f22,f32,"beta","LFV_ST_TUMuTau","Normalized Entries","|#eta|_{b}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f12,f22,f32,"mueta","LFV_ST_TUMuTau","Normalized Entries","|#eta|_{#mu}", 0.70, 0.65, 0.85, 0.9);
  
  make3LFVfilePlot(f13,f23,f33,"lepdR","LFV_TT_TCMuTau","Normalized Entries","#Delta R(#mu,#tau)", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f13,f23,f33,"lepmass","LFV_TT_TCMuTau","Normalized Entries","M(#mu,#tau)", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f13,f23,f33,"bpt","LFV_TT_TCMuTau","Normalized Entries","p_{T}_{b}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f13,f23,f33,"mupt","LFV_TT_TCMuTau","Normalized Entries","p_{T}_{#mu}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f13,f23,f33,"taupt","LFV_TT_TCMuTau","Normalized Entries","p_{T}_{#tau}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f13,f23,f33,"beta","LFV_TT_TCMuTau","Normalized Entries","|#eta|_{b}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f13,f23,f33,"mueta","LFV_TT_TCMuTau","Normalized Entries","|#eta|_{#mu}", 0.70, 0.65, 0.85, 0.9);
  
  make3LFVfilePlot(f14,f24,f34,"lepdR","LFV_TT_TUMuTau","Normalized Entries","#Delta R(#mu,#tau)", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f14,f24,f34,"lepmass","LFV_TT_TUMuTau","Normalized Entries","M(#mu,#tau)", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f14,f24,f34,"bpt","LFV_TT_TUMuTau","Normalized Entries","p_{T}_{b}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f14,f24,f34,"mupt","LFV_TT_TUMuTau","Normalized Entries","p_{T}_{#mu}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f14,f24,f34,"taupt","LFV_TT_TUMuTau","Normalized Entries","p_{T}_{#tau}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f14,f24,f34,"beta","LFV_TT_TUMuTau","Normalized Entries","|#eta|_{b}", 0.70, 0.65, 0.85, 0.9);
  make3LFVfilePlot(f14,f24,f34,"mueta","LFV_TT_TUMuTau","Normalized Entries","|#eta|_{#mu}", 0.70, 0.65, 0.85, 0.9);
  /* 
  TFile * f1 = new TFile("LFV_TT_to_cmutau_Clq_2018_GenAna_v1.root");
  TFile * f2 = new TFile("LFV_TT_to_cmutau_Clu_2018_GenAna_v1.root");
  TFile * f3 = new TFile("LFV_TT_to_cmutau_Cqe_2018_GenAna_v1.root");
  TFile * f4 = new TFile("LFV_TT_to_cmutau_Ceu_2018_GenAna_v1.root");
  TFile * f5 = new TFile("LFV_TT_to_cmutau_Clequ1_2018_GenAna_v1.root");
  TFile * f6 = new TFile("LFV_TT_to_cmutau_Clequ3_2018_GenAna_v1.root");
  TFile * f7 = new TFile("LQ_TT_to_cmutau_2018_GenAna_v1.root");
  TFile * f8 = new TFile("LFV_TT_to_cmutau_Vector_2018_GenAna_v1.root");
 
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"lepLFVdR","Normalized Entries","#Delta R(#mu,#tau)", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"lepLFVmass","Normalized Entries","M(#mu,#tau)", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"cLFVpt","Normalized Entries","p_{T} of c from LFV", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"bSMpt","Normalized Entries","p_{T} of b from SM", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"muLFVpt","Normalized Entries","p_{T} of #mu from LFV", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"tauLFVpt","Normalized Entries","p_{T} of #tau from LFV", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"cLFVeta","Normalized Entries","|#eta| of c from LFV", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"bSMeta","Normalized Entries","|#eta| of b from SM", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"muLFVeta","Normalized Entries","|#eta| of #mu from LFV", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"tauLFVeta","Normalized Entries","|#eta| of #tau from LFV", 0.75, 0.65, 0.85, 0.9);
 
  make4LFVfilePlot(f5,f8,f6,f7,"lepLFVdR","Normalized Entries","#Delta R(#mu,#tau)", 0.75, 0.65, 0.85, 0.9);
  make4LFVfilePlot(f5,f8,f6,f7,"lepLFVmass","Normalized Entries","M(#mu,#tau)", 0.75, 0.65, 0.85, 0.9);
  make4LFVfilePlot(f5,f8,f6,f7,"cLFVpt","Normalized Entries","p_{T} of c from LFV", 0.75, 0.65, 0.85, 0.9);
  make4LFVfilePlot(f5,f8,f6,f7,"bSMpt","Normalized Entries","p_{T} of b from SM", 0.75, 0.65, 0.85, 0.9);
  make4LFVfilePlot(f5,f8,f6,f7,"muLFVpt","Normalized Entries","p_{T} of #mu from LFV", 0.75, 0.65, 0.85, 0.9);
  make4LFVfilePlot(f5,f8,f6,f7,"tauLFVpt","Normalized Entries","p_{T} of #tau from LFV", 0.75, 0.65, 0.85, 0.9);
  make4LFVfilePlot(f5,f8,f6,f7,"cLFVeta","Normalized Entries","|#eta| of c from LFV", 0.75, 0.65, 0.85, 0.9);
  make4LFVfilePlot(f5,f8,f6,f7,"bSMeta","Normalized Entries","|#eta| of b from SM", 0.75, 0.65, 0.85, 0.9);
  make4LFVfilePlot(f5,f8,f6,f7,"muLFVeta","Normalized Entries","|#eta| of #mu from LFV", 0.75, 0.65, 0.85, 0.9);
  make4LFVfilePlot(f5,f8,f6,f7,"tauLFVeta","Normalized Entries","|#eta| of #tau from LFV", 0.75, 0.65, 0.85, 0.9);

  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"lepdR","Normalized Entries","#Delta R(l,l)", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"lepmass","Normalized Entries","M(l,l)", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"cpt","Normalized Entries","p_{T} of c", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"bpt","Normalized Entries","p_{T} of b", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"lep1pt","Normalized Entries","p_{T} of leading lepton", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"lep2pt","Normalized Entries","p_{T} of sub-leading lepton", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"ceta","Normalized Entries","|#eta| of c", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"beta","Normalized Entries","|#eta| of b", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"lep1eta","Normalized Entries","|#eta| of leading lepton", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"lep2eta","Normalized Entries","|#eta| of sub-leading lepton", 0.75, 0.65, 0.85, 0.9);

  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"topLFVpt","Normalized Entries","p_{T} of LFV top", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"topLFVeta","Normalized Entries","|#eta| of LFV top", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"topLFVmass","Normalized Entries","Mass of LFV top", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"topleptonicpt","Normalized Entries","p_{T} of leptonic top", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"topleptoniceta","Normalized Entries","|#eta| of leptonic top", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"topleptonicmass","Normalized Entries","Mass of leptonic top", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"tophadronicpt","Normalized Entries","p_{T} of hadronic top", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"tophadroniceta","Normalized Entries","|#eta| of hadronic top", 0.75, 0.65, 0.85, 0.9);
  make7filePlot(f1,f2,f3,f4,f5,f6,f7,"tophadronicmass","Normalized Entries","Mass of hadronic top", 0.75, 0.65, 0.85, 0.9);

  make2Plot(f1,"Topmass_Clq","topLFVmass","tophadronicmass","Normalized Entries","Mass of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f2,"Topmass_Clu","topLFVmass","tophadronicmass","Normalized Entries","Mass of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f3,"Topmass_Cqe","topLFVmass","tophadronicmass","Normalized Entries","Mass of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f4,"Topmass_Ceu","topLFVmass","tophadronicmass","Normalized Entries","Mass of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f5,"Topmass_Clequ1","topLFVmass","tophadronicmass","Normalized Entries","Mass of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f6,"Topmass_Clequ3","topLFVmass","tophadronicmass","Normalized Entries","Mass of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f7,"Topmass_LQ","topLFVmass","tophadronicmass","Normalized Entries","Mass of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  
  make2Plot(f1,"Toppt_Clq","topLFVpt","tophadronicpt","Normalized Entries","pt of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f2,"Toppt_Clu","topLFVpt","tophadronicpt","Normalized Entries","pt of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f3,"Toppt_Cqe","topLFVpt","tophadronicpt","Normalized Entries","pt of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f4,"Toppt_Ceu","topLFVpt","tophadronicpt","Normalized Entries","pt of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f5,"Toppt_Clequ1","topLFVpt","tophadronicpt","Normalized Entries","pt of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f6,"Toppt_Clequ3","topLFVpt","tophadronicpt","Normalized Entries","pt of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  make2Plot(f7,"Toppt_LQ","topLFVpt","tophadronicpt","Normalized Entries","pt of top (GeV)", 0.75, 0.65, 0.85, 0.9);
  */
  //make3Plot(f,"h_originofcharm","h_gen_top_c","h_gen_W_c","h_gen_gluon_c","Normalized Entries","GeV", 0.5, 0.75, 0.85, 0.9);
}
