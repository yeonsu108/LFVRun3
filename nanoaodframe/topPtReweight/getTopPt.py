from __future__ import print_function
from ROOT import *
import ROOT
import sys, os
from collections import OrderedDict
gROOT.SetBatch(True)
hostname = os.environ["HOSTNAME"]

years = ["2016pre", "2016post", "2017", "2018"]
dss = ["TTTo2L2Nu", "TT_LFV_TCMuTau_Scalar", "TT_LFV_TCMuTau_Vector", "TT_LFV_TCMuTau_Tensor", "TT_LFV_TUMuTau_Scalar", "TT_LFV_TUMuTau_Vector", "TT_LFV_TUMuTau_Tensor"]
basedir = "/data1/common/skimmed_NanoAOD/skim_test2/mc"
datasets = OrderedDict()
filelists = OrderedDict()

for year in years:
    for ds in dss:
        datasets[year + '_' + ds] = [os.path.join(basedir, year, ds)]

    for name, dataset in datasets.items():
      for path in dataset:
        filelists[name] = []
        if os.path.isdir(path):
          for tmps in os.listdir(path):
              filelists[name].append(os.path.join(path, tmps))

    for name, files in filelists.items():
      entries = 0
      h = TH1F('h', 'h', 40, 0, 2000)
      for file in files:
        f = TFile.Open(file,'READ')
        print("processing "+file.split("/")[-5] + " " + file.split("/")[-1], end="\r")
        tree = f.Get("Events")
        htmp1 = TH1F('htmp1', 'htmp1', 40, 0, 2000)
        htmp2 = TH1F('htmp2', 'htmp2', 40, 0, 2000)
        tree.Draw("GenPart_pt>>htmp1", "GenPart_pdgId == 6 && GenPart_statusFlags & (1 << 13)")
        tree.Draw("GenPart_pt>>htmp2", "GenPart_pdgId == -6 && GenPart_statusFlags & (1 << 13)")
        h.Add(htmp1, 1.0)
        h.Add(htmp2, 1.0)
        entries += tree.GetEntries()
        
      tmp_string = '['
      for i in range(1,h.GetNbinsX()+1):
        tmp_string += str(h.GetBinContent(i)) + ', '
      tmp_string += ']\n'
      tmp_string += str(entries)
      with open(name+'.txt', 'w') as f: f.write(tmp_string)
      h.Clear()
