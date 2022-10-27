from ROOT import *
import ROOT
import sys, os
from subprocess import check_call
from os import listdir, path
import collections
import glob
import multiprocessing

labels = ['rerun_staug22','rerun_ttaug22']

lumi_dict = {'16pre': 19500, '16post': 16800, '17': 41530, '18':59740}#run2:137570
file_names = collections.OrderedDict()

for label in labels:
  if not os.path.exists(label + "/Run2"):
    try: os.makedirs(label + "/Run2")
    except: pass

def store_file(it):
  path = it[0]
  file_name = it[1]
  for f in file_name:
    ftmp = TFile.Open(os.path.join(path, f[:f.rfind('_')] + '.root'), 'READ')

    hist_names = [x.GetName() for x in ftmp.GetListOfKeys()]
    hist_names = list(dict.fromkeys(hist_names)) #remove duplicates from more than one instances 
    hist_names[:] = [item for item in hist_names if item not in ['hcounter_nocut']]
    hist_names.sort()

    ntmp = ftmp.Get("hcounter_nocut").GetBinContent(2)

    dest_name = path.split('/')[0] + '/Run2/' + f
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

  for label in labels:
    for era in ['16pre', '16post', '17', '18']:
      dir_path = os.path.join(label, era+'_postprocess')
      dirs = os.listdir(dir_path)
      dirs[:] = [item.replace('.root', '_' + era + '.root') for item in dirs if any(i in item for i in ['LFV'])] #avoid TTTH merged
      file_names[dir_path] = dirs

  pool = multiprocessing.Pool(1)
  pool.map(store_file, file_names.items())
  pool.close()
  pool.join()

  chs = ['ST_LFV_TCMuTau_Scalar', 'ST_LFV_TCMuTau_Tensor', 'ST_LFV_TCMuTau_Vector',
         'ST_LFV_TUMuTau_Scalar', 'ST_LFV_TUMuTau_Tensor', 'ST_LFV_TUMuTau_Vector',
         'TT_LFV_TToCMuTau_Scalar', 'TT_LFV_TToCMuTau_Tensor', 'TT_LFV_TToCMuTau_Vector',
         'TT_LFV_TToUMuTau_Scalar', 'TT_LFV_TToUMuTau_Tensor', 'TT_LFV_TToUMuTau_Vector']
  #for coup in ['ST', 'TT']:
  #  for quark in ['TToCMuTau', 'TToUMuTau', 'TCMuTau', 'TUMuTau']:
  #    for rank in ['Scalar', 'Vector', 'Tensor']:
  #      chs.append(coup + '_LFV_' + quark + '_' + rank)

  for label in labels:
    for ch in chs:
      print(label + '/Run2/hist_' + ch + '_1*.root')
      check_call(['hadd','-f', label + '/Run2/hist_' + ch + '.root'] +  glob.glob(label + '/Run2/hist_' + ch + '_1*.root'))
