#include "TMath.h"
#include "TRandom3.h"
#include "ABCDmain.h"
#include <iostream>

using namespace std;

double ABCD(double A, double B, double C)
{
    return B*C/A;
}

double ABCDext5(double A, double B, double C, double Ap, double Cp, double r)
{
    return TMath::Power(C/A,1.0+r) * TMath::Power(Ap/Cp, r) * B;
}

void ABCDext5_MC(int nsamp, double A, double B, double C, double Ap, double Cp, double r)
{
    TRandom3 rn;
    double abcdsum=0.0;
    double abcdsqsum=0.0;
    double abcdextsum=0.0;
    double abcdextsqsum=0.0;
    for (int i=0; i<nsamp; i++)
    {
        double a = rn.Gaus(A, sqrt(A));
        double b = rn.Gaus(B, sqrt(B));
        double c = rn.Gaus(C, sqrt(C));
        double ap = rn.Gaus(Ap, sqrt(Ap));
        double cp = rn.Gaus(Cp, sqrt(Cp));

        double abcd = ABCD(a,b,c);
        abcdsum += abcd;
        abcdsqsum += abcd*abcd;

        double abcdext = ABCDext5(a,b,c,ap,cp,r);
        abcdextsum += abcdext;
        abcdextsqsum += abcdext*abcdext;
    }
    double abcdmean = abcdsum/nsamp;
    double abcderr = TMath::Sqrt(abcdsqsum/nsamp - abcdmean*abcdmean);

    double abcdextmean = abcdextsum/nsamp;
    double abcdexterr = TMath::Sqrt(abcdextsqsum/nsamp - abcdextmean*abcdextmean);

    cout <<"ABCD     : " << abcdmean << " +- " << abcderr << endl;
    cout <<"ABCDext  : " << abcdextmean <<" +- "<< abcdexterr << endl;
}

double ABCDext6(double A, double B, double C, double Cp, double E, double G)
{
    double abcd=ABCD(A,B,C);
    double corr=Cp * G /E;
    return TMath::Power(abcd, 4.0/3.0) / TMath::Power(corr, 1.0/3.0);
}

double ABCDext8(double A, double B, double C, double Ap, double Cp, double E, double F, double G)
{
    double abcd=ABCD(A,B,C);
    double corrx = Cp*B/Ap;
    double corry = C*G/F;
    double corrtwosteps = Cp * G/ E;

    return TMath::Power(abcd,4.0) * TMath::Power(corrx,-2.0) * TMath::Power(corry, -2.0)
        * TMath::Power(corrtwosteps, 1.0);
    
}

void ABCDmain()
{
    // njmin=7
    double A=14378.0;
    double B= 20068.0;
    double C= 2388.0;
    double D= 4874.0;
    double Ap= 15046.0;
    double Cp = 1961.0;
    double E = 63216.0;
    double F = 49685.0;
    double G = 55756.0;

    // njmin=6 nbmin=2
    /*
    double A=15046.0;
    double B= 34447.0;
    double C= 1961.0;
    double D= 7264.0;
    double Ap= 11293.0;
    double Cp = 1065.0;
    double E = 58854.0;
    double F = 63216.0;
    double G = 105442.0;
    */
    
    // njmin=6 nbmin=1
    /*
    double A= 63216.0;
    double B= 105442.0;
    double C= 17007.0;
    double D= 41711.0;
    double Ap= 58854.0;
    double Cp = 12358.0;
    double E = 74939.0;
    double F = 70900.0;
    double G = 101468.0;
    */

    cout << "True D : " << D << endl;
    cout <<"ABCD     : " << ABCD(A,B,C) << endl;
    cout <<"ABCDext  : " << ABCDext5(A,B,C,Ap,Cp) << endl;
    cout <<"ABCDext6 : " << ABCDext6(A,B,C,Cp,E,G) << endl;
    cout <<"ABCDext8 : " << ABCDext8(A,B,C,Ap,Cp,E,F,G) << endl;
    
    TRandom3 rn;
    double abcdsum=0.0;
    double abcdsqsum=0.0;
    double abcdextsum=0.0;
    double abcdextsqsum=0.0;
    double abcdext6sum=0.0;
    double abcdext6sqsum=0.0;
    double abcdext8sum=0.0;
    double abcdext8sqsum=0.0;

    int nsamp=100000;
    for (int i=0; i<nsamp; i++)
    {
        double a = rn.Gaus(A, sqrt(A));
        double b = rn.Gaus(B, sqrt(B));
        double c = rn.Gaus(C, sqrt(C));
        double d = rn.Gaus(D, sqrt(D));
        double ap = rn.Gaus(Ap, sqrt(Ap));
        double cp = rn.Gaus(Cp, sqrt(Cp));
        double e = rn.Gaus(E, sqrt(E));
        double f = rn.Gaus(F, sqrt(F));
        double g = rn.Gaus(G, sqrt(G));

        double abcd = ABCD(a,b,c);
        abcdsum += abcd;
        abcdsqsum += abcd*abcd;

        double abcdext = ABCDext5(a,b,c,ap,cp);
        abcdextsum += abcdext;
        abcdextsqsum += abcdext*abcdext;

        double abcdext6 = ABCDext6(a,b,c,cp,e,g);
        abcdext6sum += abcdext6;
        abcdext6sqsum += abcdext6*abcdext6;

        double abcdext8 = ABCDext8(a,b,c,ap,cp,e,f,g);
        abcdext8sum += abcdext8;
        abcdext8sqsum += abcdext8*abcdext8;
    }
    double abcdmean = abcdsum/nsamp;
    double abcderr = TMath::Sqrt(abcdsqsum/nsamp - abcdmean*abcdmean);

    double abcdextmean = abcdextsum/nsamp;
    double abcdexterr = TMath::Sqrt(abcdextsqsum/nsamp - abcdextmean*abcdextmean);

    double abcdext6mean = abcdext6sum/nsamp;
    double abcdext6err = TMath::Sqrt(abcdext6sqsum/nsamp - abcdext6mean*abcdext6mean);

    double abcdext8mean = abcdext8sum/nsamp;
    double abcdext8err = TMath::Sqrt(abcdext8sqsum/nsamp - abcdext8mean*abcdext8mean);

    cout <<"ABCD     : " << abcdmean << " +- " << abcderr << endl;
    cout <<"ABCDext  : " << abcdextmean <<" +- "<< abcdexterr << endl;
    cout <<"ABCDext6 : " << abcdext6mean <<" +- "<< abcdext6err << endl;
    cout <<"ABCDext8 : " << abcdext8mean <<" +- "<< abcdext8err << endl;

}

void ABCDmain2(bool merged)
{

    double A, B, C, D, Ap, Cp;

    if (!merged)
    {
        // for nb=2,3 nj=7,8,9
        A = 49685.0;
        B = 55756.0;
        C = 16766.0;
        D = 24942.0;
        Ap = 63216.0;
        Cp = 17007.0;
    }
    else
    {
        // for nb=2,3 nj=7,8,9
        A = 100690.0;
        B = 106219.0;
        C = 16766.0;
        D = 24942.0;
        Ap = 267904.0;
        Cp = 29365.0;
    }

    cout << "True D : " << D << endl;
    cout <<"ABCD     : " << ABCD(A,B,C) << endl;
    cout <<"ABCDext  : " << ABCDext5(A,B,C,Ap,Cp) << endl;
    
    TRandom3 rn;
    double abcdsum=0.0;
    double abcdsqsum=0.0;
    double abcdextsum=0.0;
    double abcdextsqsum=0.0;

    int nsamp=100000;
    for (int i=0; i<nsamp; i++)
    {
        double a = rn.Gaus(A, sqrt(A));
        double b = rn.Gaus(B, sqrt(B));
        double c = rn.Gaus(C, sqrt(C));
        double d = rn.Gaus(D, sqrt(D));
        double ap = rn.Gaus(Ap, sqrt(Ap));
        double cp = rn.Gaus(Cp, sqrt(Cp));

        double abcd = ABCD(a,b,c);
        abcdsum += abcd;
        abcdsqsum += abcd*abcd;

        double abcdext = ABCDext5(a,b,c,ap,cp);
        abcdextsum += abcdext;
        abcdextsqsum += abcdext*abcdext;

    }
    double abcdmean = abcdsum/nsamp;
    double abcderr = TMath::Sqrt(abcdsqsum/nsamp - abcdmean*abcdmean);

    double abcdextmean = abcdextsum/nsamp;
    double abcdexterr = TMath::Sqrt(abcdextsqsum/nsamp - abcdextmean*abcdextmean);

    cout <<"ABCD     : " << abcdmean << " +- " << abcderr << endl;
    cout <<"ABCDext  : " << abcdextmean <<" +- "<< abcdexterr << endl;

}

