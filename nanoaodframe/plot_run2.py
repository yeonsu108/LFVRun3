import sys, os
import re
from subprocess import call
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-I', '--input', dest='input', type=str, default="test")
parser.add_argument("-D", dest="DNN", action="store_true", default=False, help="Run for DNN histograms")
args = parser.parse_args()
input = args.input


config_path = '../plotIt/configs/'
common_syst = 'systematics:\n'
groups = ['GData', 'Gttll', 'Gttlj', 'Gttjj', 'GttV', 'GZJets', 'GWJets', 'GSingleT', 'GVV', 'GQCD',
          'GLFVSTcv', 'GLFVSTuv', 'GLFVTTcv', 'GLFVTTuv',]
years = {'2016pre': 19502, '2016post': 16812, '2017': 41480, '2018':59832}

common_syst_list = []
for year, lumi in years.items():
  with open(config_path + 'config_' + year + '.yml') as f:
    lines = f.readlines()
    for line in lines:
      if "  - " in line: common_syst_list.append(line)

common_syst_list = sorted(set(common_syst_list), key=common_syst_list.index)

dest_path = input
if not os.path.exists(os.path.join(dest_path, 'figure_run2')):
  try: os.makedirs(os.path.join(dest_path, 'figure_run2'))
  except: pass
if not os.path.exists(os.path.join(dest_path, 'figure_run2/qcd')):
  try: os.makedirs(os.path.join(dest_path, 'figure_run2/qcd'))
  except: pass
if not os.path.exists(os.path.join(dest_path, 'figure_run2/dyincl')):
  try: os.makedirs(os.path.join(dest_path, 'figure_run2/dyincl'))
  except: pass
if not os.path.exists(os.path.join(dest_path, 'figure_run2/dyincl/qcd')):
  try: os.makedirs(os.path.join(dest_path, 'figure_run2/dyincl/qcd'))
  except: pass

for item in common_syst_list:
  common_syst += item

string_for_files = ''
for year, lumi in years.items():
  #Firstly, merge file list + scale
  with open(config_path + 'files_' + year + '.yml') as f:
    lines = f.readlines()
    skip_signal = False
    for line in lines:
      #if '#' in line[0]: line = line[1:]
      if skip_signal and 'hist' in line: skip_signal = False
      if 'LFV' in line: skip_signal = True
      #if 'hist_QCD' in line: skip_signal = True
      if '#' in line[0]: skip_signal = True
      if 'hist' in line:
        line = line[0] + dest_path + '/' + year + '_postprocess/' + line[1:]
        if not any(i in line for i in ['LFV', 'SingleMuon']):
          line += '  scale: ' + str(int(lumi)/137570.0) + '\n'
      #if not skip_signal and not any(i in line for i in ['yields-group']):
      if not skip_signal:
        #if 'group' in line and not any(i in line for i in groups): string_for_files += '  group: Gother \n'
        #else: string_for_files += line
        string_for_files += line


with open(config_path + 'files_Run2.yml', 'w+') as fnew:
  print("""
'{0}/Run2/hist_ST_LFV_TCMuTau_Vector.root':
  type: signal
  pretty-name: 'LFVSTcv'
  cross-section: 0.0368
  #generated-events: 7789000.0
  group: GLFVSTcv
  order: 1

'{0}/Run2/hist_ST_LFV_TUMuTau_Vector.root':
  type: signal
  pretty-name: 'LFVSTuv'
  cross-section: 0.393
  #generated-events: 7887981.0
  group: GLFVSTuv
  order: 2

'{0}/Run2/hist_TT_LFV_TCMuTau_Vector.root':
  type: signal
  pretty-name: 'LFVTTcv'
  cross-section: 0.0215
  #generated-events: 6355000.0
  group: GLFVTTcv
  order: 3

'{0}/Run2/hist_TT_LFV_TUMuTau_Vector.root':
  type: signal
  pretty-name: 'LFVTTuv'
  cross-section: 0.0215
  #generated-events: 11286000.0
  group: GLFVTTuv
  order: 4
  """.format(dest_path), file=fnew)
  fnew.write(string_for_files)

with open(config_path + 'template_Run2.yml') as f:
  lines = f.readlines()
  with open(config_path + 'config_Run2.yml', 'w+') as f1:
    for line in lines: f1.write(line)
    f1.write(common_syst)
    if 'FF' in dest_path:
        f1.write("\nplots:\n  include: ['histos_FFapply.yml', 'histos_yield_S5.yml']\n")
    elif options.DNN:
        f1.write("\nplots:\n  include: ['histos_dnn.yml']\n")
    else:
        f1.write("\nplots:\n  include: ['histos_control.yml', 'histos_reco.yml', 'histos_yield.yml']\n")

call(['../plotIt/plotIt', '-o ' + dest_path + '/figure_run2', config_path + 'config_Run2.yml', '-y', '-s'], shell=False)
call(['../plotIt/plotIt', '-o ' + dest_path + '/figure_run2/qcd', config_path + 'config_Run2.yml', '-y', '-s'], shell=False)
call(['../plotIt/plotIt', '-o ' + dest_path + '/figure_run2/dyincl', config_path + 'config_Run2.yml', '-y', '-s', '-d'], shell=False)
call(['../plotIt/plotIt', '-o ' + dest_path + '/figure_run2/dyincl/qcd', config_path + 'config_Run2.yml', '-y', '-s', '-d', '-q'], shell=False)
