import sys
import os
import csv

def readfile(logfile):
    out = [0] * 5
    with open(logfile,'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            if "Expected" in line:
                if "2.5%" in line:
                    out[3] = float(line.split(" ")[-1])
                elif "16.0%" in line:
                    out[1] = float(line.split(" ")[-1])
                elif "50.0%" in line:
                    out[0] = float(line.split(" ")[-1])
                elif "84.0%" in line:
                    out[2] = float(line.split(" ")[-1])
                elif "97.5%" in line:
                    out[4] = float(line.split(" ")[-1])
    return out

years = ["run16APV","run16","run17","run18"]
ops = ["c_s","c_v","c_t","u_s","u_v","u_t"]
cats = ["cat1","cat2","combined"]
with open('limits_mar02.csv','w') as f:
    wr = csv.writer(f)
    head = ["Year","Category","Operator","central","-1sig","+1sig","-2sig","+2sig"]
    wr.writerow(head)
    for year in years:
        for cat in cats:
            for op in ops:
                logfile = "logs/result_"+cat+"_"+year+"_"+op+".txt"
                print(logfile)
                tmp = []
                tmp.append(year)
                tmp.append(cat)
                tmp.append(op)
                tmp += readfile(logfile)
                wr.writerow(tmp)
                print(tmp)
    for op in ops:
        logfile = "logs/result_combined_run2_"+op+".txt"
        print(logfile)
        tmp = []
        tmp.append("run2")
        tmp.append(cat)
        tmp.append(op)
        tmp += readfile(logfile)
        wr.writerow(tmp)
        print(tmp)

