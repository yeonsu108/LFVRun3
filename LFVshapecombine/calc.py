import sys
import os
import csv
import math
import numpy as np
import itertools

def readFile(logfile):
    out = [0] * 3
    with open(logfile,'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            if "Expected" in line:
                if "16.0%" in line:
                    out[0] = float(line.split(" ")[-1])
                elif "50.0%" in line:
                    out[1] = float(line.split(" ")[-1])
                elif "84.0%" in line:
                    out[2] = float(line.split(" ")[-1])
    return out

def calcXsec(op,limits):
    out = []
    if op == "c_s":
        out = np.array(limits) * 10.09
    elif op == "c_v":
        out = np.array(limits) * 58.3
    elif op == "c_t":
        out = np.array(limits) * 307.4
    elif op == "u_s":
        out = np.array(limits) * 86.49
    elif op == "u_v":
        out = np.array(limits) * 414.5
    elif op == "u_t":
        out = np.array(limits) * 1925
    return list(out)

def calcWilson(limits):
    return list(np.sqrt(limits))

def calcBr(op, limits):
    out = []
    if op == "c_s" or op == "u_s":
        out = 2*np.array(limits)*(172.5**5)*10**(-6)/(6144*(math.pi**3))
    elif op == "c_v" or op == "u_v":
        out = np.array(limits)*(172.5**5)*10**(-6)/(1536*(math.pi**3))
    elif op == "c_t" or op == "u_t":
        out = 2*np.array(limits)*(172.5**5)*10**(-6)/(128*(math.pi**3))
    return list(out)

years = ["run16APV","run16","run17","run18","run2"]
#years = ["run2"]
cats = ["cat1","cat2","combined"]
ops = ["c_s","c_v","c_t","u_s","u_v","u_t"]



totalLimits = []
for year in years:
    for cat in cats:
        if year == "run2" and cat != "combined": continue
        for op in ops:
            logfile = "logs/result_"+cat+"_"+year+"_"+op+".txt"
            limits = readFile(logfile)
            calcLimits = []
            calcLimits = calcXsec(op,limits)
            calcLimits += calcWilson(limits)
            calcLimits += calcBr(op,limits)
            totalLimits.append(calcLimits)
    totalnom = np.array(totalLimits)[:,1::3].tolist()
    totalerr = np.delete(totalLimits, [1,4,7], axis=1).tolist()
    total = [ j + totalerr[i] for i,j in enumerate(totalnom) ]
    newtotal = list(itertools.chain(*total))
    header = "\\begin{table}[!hp] \n\
    \\centering \n\
    \\renewcommand{\\arraystretch}{1.1} \n\
    \\begin{tabular}{c|c|c|c|c|c} \n\
        \\hline\\hline \n\
        Category & Interaction & Type & $\\sigma$ [fb] & $C_{tq\\mu\\tau}\\slash\\Lambda^{2}$ [$TeV^{-2}$] & $Br(t\\to q\\mu\\tau)\\times 10^{-6}$ \\\\ \\hline\\hline"
    print(header)
    if year == "run2":
        body ="        \\multirow{{12}}{{*}}{{Combined}} & \\multirow{{6}}{{*}}{{$tc\\mu\\tau$}} & \\multirow{{2}}{{*}}{{Scalar}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Vector}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Tensor}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & \\multirow{{6}}{{*}}{{$tu\\mu\\tau$}} & \\multirow{{2}}{{*}}{{Scalar}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Vector}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Tensor}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
        \\hline\\hline".format(*newtotal)
        print(body)
    else:
        body ="        \\multirow{{12}}{{*}}{{Category 1}} & \\multirow{{6}}{{*}}{{$tc\\mu\\tau$}} & \\multirow{{2}}{{*}}{{Scalar}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Vector}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Tensor}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & \\multirow{{6}}{{*}}{{$tu\\mu\\tau$}} & \\multirow{{2}}{{*}}{{Scalar}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Vector}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Tensor}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
        \\multirow{{12}}{{*}}{{Category 2}} & \\multirow{{6}}{{*}}{{$tc\\mu\\tau$}} & \\multirow{{2}}{{*}}{{Scalar}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Vector}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Tensor}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & \\multirow{{6}}{{*}}{{$tu\\mu\\tau$}} & \\multirow{{2}}{{*}}{{Scalar}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Vector}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Tensor}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
        \\multirow{{12}}{{*}}{{Combined}} & \\multirow{{6}}{{*}}{{$tc\\mu\\tau$}} & \\multirow{{2}}{{*}}{{Scalar}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Vector}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Tensor}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & \\multirow{{6}}{{*}}{{$tu\\mu\\tau$}} & \\multirow{{2}}{{*}}{{Scalar}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Vector}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
         & & \\multirow{{2}}{{*}}{{Tensor}} & {:.4f} & {:.4f} & {:.4f} \\\\ \n\
        & & & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}] & [{:.4f}, {:.4f}]\\\\ \\cline{{3-6}} \n\
        \\hline\\hline".format(*newtotal)
        print(body)
    bottom = "    \\end{tabular} \n\
    \\caption{Table for "+year+" combined upper limits of LFV cross section ($\\sigma$), Wilson Coefficient ($C_{tq\\mu\\tau}$), and branching fraction for different types of interactions. $\\pm1\\sigma$ values are in brackets.} \n\
    \\label{tab:"+year+"limit} \n\
\\end{table}"
    print(bottom)

"""
        \multirow{12}{*}{Category 1} & \multirow{6}{*}{$tc\mu\tau$} & \multirow{2}{*}{Scalar} & 6.819 & 0.8221 & 1.084 \\ 
        & & & [4.577, 10.41] & [0.6735, 1.016] & [0.7274, 1.654]\\ \cline{3-6} 
         & & \multirow{2}{*}{Vector} & 9.281 & 0.399 & 0.5106 \\ 
        & & & [6.25, 14.2] & [0.3274, 0.4936] & [0.3438, 0.7812]\\ \cline{3-6} 
         & & \multirow{2}{*}{Tensor} & 11.56 & 0.1939 & 2.894 \\ 
        & & & [7.808, 17.83] & [0.1594, 0.2408] & [1.955, 4.464]\\ \cline{2-6} 
         & \multirow{6}{*}{$tu\mu\tau$} & \multirow{2}{*}{Scalar} & 4.645 & 0.2317 & 0.08611 \\ 
        & & & [3.088, 7.127] & [0.1889, 0.2871] & [0.05725, 0.1321]\\ \cline{3-6} 
         & & \multirow{2}{*}{Vector} & 5.471 & 0.1149 & 0.04233 \\ 
        & & & [3.482, 8.083] & [0.09165, 0.1396] & [0.02694, 0.06254]\\ \cline{3-6} 
         & & \multirow{2}{*}{Tensor} & 9.047 & 0.06856 & 0.3618 \\ 
        & & & [6.545, 11.94] & [0.05831, 0.07874] & [0.2617, 0.4772]\\ \cline{1-6} 

        \multirow{12}{*}{Category 2} & \multirow{6}{*}{$tc\mu\tau$} & \multirow{2}{*}{Scalar} & 382.8 & 6.159 & 60.83 \\ 
        & & & [268.4, 555.2] & [5.157, 7.418] & [42.65, 88.23]\\ \cline{3-6} 
         & & \multirow{2}{*}{Vector} & 274.2 & 2.169 & 15.08 \\ 
        & & & [192.2, 397.7] & [1.816, 2.612] & [10.57, 21.88]\\ \cline{3-6} 
         & & \multirow{2}{*}{Tensor} & 196.9 & 0.8004 & 49.31 \\ 
        & & & [137.3, 285.6] & [0.6684, 0.964] & [34.38, 71.52]\\ \cline{2-6} 
         & \multirow{6}{*}{$tu\mu\tau$} & \multirow{2}{*}{Scalar} & 2,368 & 5.232 & 43.9 \\ 
        & & & [1,660, 3,434] & [4.381, 6.301] & [30.77, 63.67]\\ \cline{3-6} 
         & & \multirow{2}{*}{Vector} & 1,289 & 1.763 & 9.972 \\ 
        & & & [903.5, 1,869] & [1.476, 2.124] & [6.991, 14.46]\\ \cline{3-6} 
         & & \multirow{2}{*}{Tensor} & 483.2 & 0.501 & 19.32 \\ 
        & & & [337.5, 702.6] & [0.4187, 0.6042] & [13.49, 28.09]\\ \cline{1-6}

        \multirow{12}{*}{Combined} & \multirow{6}{*}{$tc\mu\tau$} & \multirow{2}{*}{Scalar} & 6.799 & 0.8209 & 1.08 \\ 
        & & & [4.564, 10.4] & [0.6725, 1.015] & [0.7253, 1.653]\\ \cline{3-6} 
         & & \multirow{2}{*}{Vector} & 9.281 & 0.399 & 0.5106 \\ 
        & & & [6.226, 14.16] & [0.3268, 0.4928] & [0.3425, 0.779]\\ \cline{3-6} 
         & & \multirow{2}{*}{Tensor} & 11.56 & 0.1939 & 2.894 \\ 
        & & & [7.839, 17.74] & [0.1597, 0.2402] & [1.963, 4.441]\\ \cline{2-6} 
         & \multirow{6}{*}{$tu\mu\tau$} & \multirow{2}{*}{Scalar} & 4.645 & 0.2317 & 0.08611 \\ 
        & & & [3.088, 7.127] & [0.1889, 0.2871] & [0.05725, 0.1321]\\ \cline{3-6} 
         & & \multirow{2}{*}{Vector} & 5.471 & 0.1149 & 0.04233 \\ 
        & & & [3.482, 8.083] & [0.09165, 0.1396] & [0.02694, 0.06254]\\ \cline{3-6} 
         & & \multirow{2}{*}{Tensor} & 8.855 & 0.06782 & 0.3541 \\ 
        & & & [6.545, 12.9] & [0.05831, 0.08185] & [0.2617, 0.5157]\\ \cline{1-6} 
        \hline\hline 
\end{table}"""
