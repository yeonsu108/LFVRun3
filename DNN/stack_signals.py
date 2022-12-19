from ROOT import *
import ROOT
import sys, os
from subprocess import check_call
from os import listdir, path
import collections
import glob
import multiprocessing
import argparse

#labels = ['rerun_multi_Multiaug22','rerun_staug22','rerun_ttaug22']
parser = argparse.ArgumentParser()
parser.add_argument('-L', '--label', dest='label', type=str, default="rerun_staug22")
parser.add_argument('-D', '--discriminator', dest='discriminator', type=str, default="")
parser.add_argument('-A', '--alpha', dest='alpha', type=str, default="")
args = parser.parse_args()
label = args.label
discriminator = args.discriminator
alpha = args.alpha

lumi_dict = {'16pre': 19502, '16post': 16812, '17': 41480, '18':59832}#16: 36314, run2:137625
file_names = collections.OrderedDict()

if not os.path.exists(label +"/" +discriminator + "/" + alpha + "/Run2/"):
  try: os.makedirs(label + "/" +discriminator + "/" + alpha + "/Run2/")
  except: pass

def store_file(it):
  path = it[0]
  file_name = it[1]
  for f in file_name:
    print(os.path.join(path, f[:f.rfind('_')] + '.root'))
    ftmp = TFile.Open(os.path.join(path, f[:f.rfind('_')] + '.root'), 'READ')

    hist_names = [x.GetName() for x in ftmp.GetListOfKeys()]
    hist_names = list(dict.fromkeys(hist_names)) #remove duplicates from more than one instances 
    hist_names[:] = [item for item in hist_names if item not in ['hcounter_nocut']]
    hist_names.sort()

    ntmp = ftmp.Get("hcounter_nocut").GetBinContent(2)

    dest_name = path.split('/')[0] + '/' +discriminator + "/" + alpha + '/Run2/' + f
    dest = TFile.Open(dest_name, 'RECREATE')

    print('Writing scaled histogram to ' + dest_name)

    for hist in hist_names:
      htmp = ftmp.Get(hist)
      htmp.Scale(lumi_dict[path.split('/')[1].split('_')[0]]/ntmp)
      dest.cd()
      htmp.Write()
    dest.Write()
    dest.Close()


if __name__ == '__main__':

  for era in ['16pre', '16post', '17', '18']:
     dir_path = os.path.join(label, era+'_postprocess', discriminator , alpha)
     dirs = os.listdir(dir_path)
     print("POST process path: " , dir_path)
     dirs[:] = [item.replace('.root', '_' + era + '.root') for item in dirs if any(i in item for i in ['LFV'])] #avoid TTTH merged
     print("EDITED DIRS: " , dirs)
     file_names[dir_path] = dirs

  pool = multiprocessing.Pool(1)
  pool.map(store_file, file_names.items())
  pool.close()
  pool.join()

  chs = ['ST_LFV_TCMuTau_Scalar', 'ST_LFV_TCMuTau_Tensor', 'ST_LFV_TCMuTau_Vector',
         'ST_LFV_TUMuTau_Scalar', 'ST_LFV_TUMuTau_Tensor', 'ST_LFV_TUMuTau_Vector',
         'TT_LFV_TToCMuTau_Scalar', 'TT_LFV_TToCMuTau_Tensor', 'TT_LFV_TToCMuTau_Vector',
         'TT_LFV_TToUMuTau_Scalar', 'TT_LFV_TToUMuTau_Tensor', 'TT_LFV_TToUMuTau_Vector']

  for ch in chs:
    print(label + "/" + discriminator + "/" + alpha +  '/Run2/hist_' + ch + '_1*.root')
    check_call(['hadd','-f', label + '/' + discriminator + "/" + alpha + '/Run2/hist_' + ch + '.root'] +  glob.glob(label + '/' + discriminator + "/" + alpha + '/Run2/hist_' + ch + '_1*.root'))
