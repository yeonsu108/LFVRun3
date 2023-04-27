void massfit(const char * infile, const char * histname, double m1, double w1, const char * outfile){
    TFile *_file0 = TFile::Open(infile);
    TH1F *h0=(TH1F*)_file0->Get(histname);

    TF1 * mygaus = new TF1("mygaus", "[0]/(sqrt(2.0*3.14151927)*[2])*exp(-(x-[1])*(x-[1])/(2.0*[2]*[2]))", 50, 250);
    mygaus->SetParName(0, "Number of signal");
    mygaus->SetParName(1, "Mean");
    mygaus->SetParName(2, "Width");
    double initval1[3] = { 2500, 151, 2.4};
    mygaus->SetParameters(initval1);
    
    TF1 * mybw = new TF1("mybw","[0]*TMath::BreitWigner(x, [1], [2])", 0, 150);
    mybw->SetParName(0, "Number of signal");
    mybw->SetParName(1, "Mean");
    mybw->SetParName(2, "Gamma");
    double initval2[3] = {5000.0, 172, 2};
    mybw->SetParameters(initval2);
    
    TF1 * myvoigt = new TF1("myvoigt","[0]*TMath::Voigt(x-[1], [2], [3])", 50, 250);
    myvoigt->SetParName(0, "Number of signal");
    myvoigt->SetParName(1, "Mean");
    myvoigt->SetParName(2, "Width");
    myvoigt->SetParName(3, "Gamma");
    double initval3[4] = {10000.0, m1 ,w1 , 3};
    myvoigt->SetParameters(initval3);
    
    TCanvas *MyC=new TCanvas("MyC","invariant mass",700,500);
    //h0->Fit(mygaus, "R");
    //h0->Fit(mybw, "R");
    gStyle->SetOptTitle(0);
//    gStyle->SetStatStyle(1000);
//    gStyle->SetStatX(0.87);
//    gStyle->SetStatY(0.85);
//    gStyle->SetStatBorderSize(0);
    gStyle->SetOptStat(0);
    //gStyle->SetOptFit(101);
//    h0->SetStats(kFALSE);
    h0->GetXaxis()->SetLabelSize(0.07);
    h0->GetYaxis()->SetLabelSize(0.06);
    h0->Fit(myvoigt, "R");
    h0->SetLineWidth(2);
    h0->Draw();

    TF1 *fit = h0->GetFunction("myvoigt");
    double fit_mean = fit->GetParameter(1);
    double fit_width = fit->GetParameter(2);

    TString s1 = "Mean : "+TString::LLtoa(fit_mean, 10)+" GeV";
    TString s2 = "Width : "+TString::LLtoa(fit_width, 10)+" GeV";

    TPaveText *pt1 = new TPaveText(0.65,0.4,0.8,0.7,"NDC");
    pt1->SetBorderSize(0);
    pt1->SetFillColor(0);
    pt1->SetTextSize(0.07);
    pt1->AddText("Voigt Fitting");
    pt1->AddText(s1.Data());
    pt1->AddText(s2.Data());
    pt1->Draw();
    
    MyC->Print(outfile);
}

