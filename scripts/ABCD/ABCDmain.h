#ifndef ABCDmain_H
double ABCD(double A, double B, double C);
double ABCDext5(double A, double B, double C, double Ap, double Cp, double r=1.0);
void ABCDext5_MC(int ntrials, double A, double B, double C, double Ap, double Cp, double r=1.0);
double ABCDext6(double A, double B, double C, double Cp, double E, double G);
double ABCDext8(double A, double B, double C, double Ap, double Cp, double E, double F, double G);
#define ABCDmain_H
#endif
