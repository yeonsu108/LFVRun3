#!/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:01:46 2018

@author: Suyong Choi (Department of Physics, Korea University suyong@korea.ac.kr)
@refactored for LFV analysis: Jiwon Park (jiwon.park@cern.ch)

"""
import sys, os, re, string, argparse
import subprocess


from importlib import import_module
import multiprocessing
import cppyy
import ROOT
    
#def Nanoaodprocessor_singledir(outputroot, indir, year, syst, json, saveallbranches):
def Nanoaodprocessor_singledir(inputs):

    outputroot = inputs[0]
    indir = inputs[1]
    year = inputs[2]
    syst = inputs[3]
    json = inputs[4]
    saveallbranches = inputs[5]

    #sys.stdout = open(outputroot.replace(year, year + '/log').replace('.root', '.out'), "w")

    print("Input: " + indir + ", " + "Output: " + outputroot + ", Syst: " + syst + "\n")

    if not re.match('.*\.root', outputroot):
        print("Output file should be a root file! Quitting")
        exit(-1)

    fullnamelist =[]
    rootfilestoprocess = []
    print("collecting root files in "+indir)
    flist = os.listdir(indir)
    if len(flist) == 0:
        print("No file found in," + indir + ", ending processing")
        return
    for fname in flist:
        fullname = os.path.join(indir, fname)
        fullnamelist.append(fullname)

    for fname in fullnamelist:            
        if re.match('.*\.root', fname) and os.path.isfile(fname): # if it has .root file extension
            rootfilestoprocess.append(fname)
    print("files to process")
    print(rootfilestoprocess)
    t = ROOT.TChain("Events")
    for afile in rootfilestoprocess:
        t.Add(afile)
    aproc = None
    aproc = ROOT.TopLFVAnalyzer(t, outputroot, year, syst, json, "", 1)
    aproc.setupAnalysis()
    aproc.run(saveallbranches, "Events")

    # process input rootfiles to sum up all the counterhistograms
    counterhistogramsum = None
    for arootfile in rootfilestoprocess:
        intf = ROOT.TFile(arootfile)
        counterhistogram = intf.Get("hcounter")
        if counterhistogram != None:
            if counterhistogramsum == None:
                counterhistogramsum = counterhistogram.Clone()
                counterhistogramsum.SetDirectory(0)
            else:
                counterhistogramsum.Add(counterhistogram)
        intf.Close()
    if counterhistogramsum != None:
        print("Updating with counter histogram")
        outf = ROOT.TFile(outputroot, "UPDATE")
        counterhistogramsum.Write()
        outf.Write("", ROOT.TObject.kOverwrite)
        outf.Close()
    else:
        print("counter histogram not found")

    pass

if __name__=='__main__':
    
    parser = argparse.ArgumentParser(usage="%prog [options]")
    parser.add_argument("-V", "--version", dest="version", type=str, default="", help="Skim version: folder under /data1/common/skimmed_NanoAOD/")
    parser.add_argument("-O", "--outdir", dest="outdir", type=str, default="", help="Output folder in your working directory")
    parser.add_argument("-Y", "--year", dest="year", type=str, default="", help="Select 2016pre, 2016post, 2017, or 2018 runs")
    parser.add_argument("-S", "--syst", dest="syst", type=str, default="theory", help="Systematic: 'data' for Data, 'nosyst' for mc without uncertainties. Default is 'theory'. To run without theory unc for TT samples, put 'all'.")
    parser.add_argument("-D", "--dataset", dest="dataset", action="store", nargs="+", default=[], help="Put dataset folder name (eg. TTTo2L2Nu) to process specific one.")
    parser.add_argument("-F", "--dataOrMC", dest="dataOrMC", type=str, default="", help="data or mc flag, if you want to process data-only or mc-only")
    options = parser.parse_args()

    year = options.year
    workdir = os.getcwd()
    indir = os.path.join('/data1/common/skimmed_NanoAOD/', options.version)
    tgdir = os.path.join(workdir, options.outdir, year)
    log = os.path.join(workdir, options.outdir, year, 'log')

    os.makedirs(tgdir, exist_ok=True)
    os.makedirs(log, exist_ok=True)

    datadir = os.path.join(indir, 'data', year)
    data_list = [os.path.join(datadir, s) for s in os.listdir(datadir)]
    mcdir = os.path.join(indir, 'mc', year)
    mc_list = [os.path.join(mcdir, s) for s in os.listdir(mcdir)]

    dataset_list = data_list + mc_list

    #syst_list = ["", "__jerup","__jerdown", "__jesAbsoluteup","__jesAbsolutedown",
    #             "__jesAbsolute_"+year[:4]+"up", "__jesAbsolute_"+year[:4]+"down",
    #             "__jesBBEC1up", "__jesBBEC1down", "__jesBBEC1_"+year[:4]+"up", "__jesBBEC1_"+year[:4]+"down",
    #             "__jesFlavorQCDup", "__jesFlavorQCDdown", "__jesRelativeBalup", "__jesRelativeBaldown",
    #             "__jesRelativeSample_"+year[:4]+"up", "__jesRelativeSample_"+year[:4]+"down"]
    syst_list = ["__jerup","__jerdown"]
    # tune and hdamp will appear as an individual dataset.
    syst_ext = ["__tuneup", "__tunedown", "__hdampup", "__hdampdown",]

    # Default syst for MC = "theory" = all SF + theory
    # To run central values only, pass "nosyst"
    # To calculate theory uncertainties (PDF, ME, PS, if available), put 'theory'
    # Data should use systematic flag "data" not to construct event weights

    # load compiled C++ library into ROOT/python
    cppyy.load_reflection_info("libnanoadrdframe.so")

    parameters = []
    for ds in dataset_list:

        if len(options.dataset) > 0 and not any(i in ds for i in options.dataset): continue

        for src in syst_list:

            if options.dataOrMC == 'data':
                if 'data' not in ds[5:]: continue
            elif options.dataOrMC == 'mc':
                if 'mc' not in ds[5:]: continue

            dataset_name = ds.split('/')[-1]
            outfname = os.path.join(tgdir, dataset_name + src + '.root')

            if 'data' in ds[5:]:
                if src == "":
                    if "2016" in ds:
                        json = os.path.join(workdir, "data/GoldenJSON/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt")
                    elif "2017" in ds:
                        json = os.path.join(workdir, "data/GoldenJSON/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.txt")
                    elif "2018" in ds:
                        json = os.path.join(workdir, "data/GoldenJSON/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt")

                    parameters.append((outfname, ds, year, "data", json, False))

                else: continue

            else:
               if src == "":
                  if options.syst == "all":
                      parameters.append((outfname, ds, year, "all", "", False))
                  elif options.syst == "theory":
                      if any(i in dataset_name for i in ["TTTo", "TT_LFV", "ST_LFV"]): #include TTW,TTZ for theory unc?
                          parameters.append((outfname, ds, year, "theory", "", False))
                      else: parameters.append((outfname, ds, year, "all", "", False))
                  elif options.syst == "nosyst":
                      parameters.append((outfname, ds, year, "nosyst", "", False))
               else:
                  #os.makedir(os.path.join(tgdir, dataset_name+src)
                  if any(i in dataset_name for i in syst_ext): continue
                  parameters.append((outfname, ds, year, src[2:], "", False))
    #for i in parameters: print(i)

    pool = multiprocessing.Pool(os.cpu_count()-2) #room for cpu
    #pool = multiprocessing.Pool(1)
    pool.map(Nanoaodprocessor_singledir, parameters)
    pool.close()
    pool.join()

    # although it says outdir, it should really be a output ROOT file name
    #Nanoaodprocessor_singledir(tgdir, indir, options.year, options.syst, json, False)
