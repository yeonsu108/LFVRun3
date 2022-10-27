import sys, os
import re
from subprocess import call

config_path = '../plotIt/configs/'
common_syst = 'systematics:\n'
groups = ['GData', 'Gttll', 'Gttlj', 'Gttjj', 'GttV', 'GZJets', 'GWJets', 'GSingleT', 'GVV', 'GQCD',
          'GLFVSTcv', 'GLFVSTuv', 'GLFVTTcv', 'GLFVTTuv',]
#not include prefire and elzvtx which exist only in 2017
#common_syst_list = ['pu', 'muid', 'muiso', 'mutrg', 'elid', 'elreco', 'eltrg',
common_syst_list = ['pu', 'btaglf', 'btaghf', 'btaglfstat1',
                    'btaglfstat2', 'btaghfstat1', 'btaghfstat2', 'btagcferr1', 'btagcferr2',
                    'jesAbsolute', 'jesBBEC1', 'jesEC2', 'jesFlavorQCD', 'jesRelativeBal']
syst = ['jesAbsoluteyear', 'jesBBEC1year', 'jesEC2year', 'jesRelativeSampleyear']

years = {'16pre':19500, '16post':16800, '17':41529, '18':59741}

for sy in syst:
  if 'year' in sy:
    for year in years.keys():
      common_syst_list.append(sy.replace('year', year))
  else: common_syst_list.append(sy)

reco_str = 'rerun_CHaug22/'
chs = ['st', 'tt']

for i in chs:
  dest_path = reco_str.replace('CH', i)
  if not os.path.exists(dest_path + 'figures'):
    try: os.makedirs(dest_path + 'figures')
    except: pass
  if not os.path.exists(dest_path + 'figures/qcd'):
    try: os.makedirs(dest_path + 'figures/qcd')
    except: pass

for item in common_syst_list:
  common_syst += '  - ' + item + '\n'

for ch in chs:
  string_for_files = ''
  dest_path = reco_str.replace('CH', ch)

  for year, lumi in years.items():
    #Firstly, merge file list + scale
    with open(config_path + 'files_' + year + '.yml') as f:
      lines = f.readlines()
      skip_signal = False
      for line in lines:
        #if '#' in line[0]: line = line[1:]
        if skip_signal and 'hist' in line: skip_signal = False
        if 'LFV' in line: skip_signal = True
        if 'hist_QCD' in line: skip_signal = True
        if '#' in line[0]: skip_signal = True
        if 'hist' in line:
          line = line[0] + dest_path+ year + '_postprocess/' + line[1:]
          if not any(i in line for i in ['LFV', 'Run1']):
            line += '  scale: ' + str(int(lumi)/137570.0) + '\n'
        if not skip_signal and not any(i in line for i in ['yields-group']):
          if 'group' in line and not any(i in line for i in groups): string_for_files += '  group: Gother \n'
          else: string_for_files += line

    file_syst = ''
    with open(config_path + 'config_' + year + '.yml') as f:
      lines = f.readlines()
      for line in lines:
        if 'type' in line:
          if 'const' in line:
            file_syst += line[:line.find(':')] + '_' + year + line[line.find(':'):line.find('hist')] + year + '_postprocess/' + line[line.find('hist'):]
          elif 'shape' in line:
            file_syst += line[:line.find('hist')] + year + '_postprocess/' + line[line.find('hist'):]


  with open(config_path + 'files_Run2.yml', 'w+') as fnew:
    print("""
'{0}Run2/hist_ST_LFV_TCMuTau_Vector.root':
  type: signal
  pretty-name: 'LFVSTcv'
  cross-section: 0.0368
  generated-events: 12645000
  group: GLFVSTcv
  order: 1

'{0}Run2/hist_ST_LFV_TUMuTau_Vector.root':
  type: signal
  pretty-name: 'LFVSTuv'
  cross-section: 0.393
  generated-events: 12785962
  group: GLFVSTuv
  order: 2

'{0}Run2/hist_TT_LFV_TToCMuTau_Vector.root':
  type: signal
  pretty-name: 'LFVTTcv'
  cross-section: 0.0215
  generated-events: 9725000
  group: GLFVTTcv
  order: 3

'{0}Run2/hist_TT_LFV_TToUMuTau_Vector.root':
  type: signal
  pretty-name: 'LFVTTuv'
  cross-section: 0.0215
  generated-events: 11286000
  group: GLFVTTuv
  order: 4
    """.format(dest_path), file=fnew)
    fnew.write(string_for_files)


  with open(config_path + 'template_Run2.yml') as f:
    lines = f.readlines()
    with open(config_path + 'config_Run2.yml', 'w+') as f1:
      for line in lines: f1.write(line)
      f1.write(common_syst)
      f1.write(file_syst)
      f1.write("\nplots:\n  include: ['histos_dnn.yml']\n")

  call(['../plotIt/plotIt', '-o ' + dest_path + '/figures', config_path + 'config_Run2.yml'], shell=False)


  #For QCD
  string_for_qcd = ''
  for year, lumi in years.items():
    with open(config_path + 'files_' + year + '.yml') as f:
      lines = f.readlines()
      skip_signal = True
      for line in lines:
        #if '#' in line[0]: line = line[1:]
        if '#' in line[0]: skip_signal = True
        if skip_signal and 'hist_QCD' in line: skip_signal = False
        if 'hist_QCD' in line:
          line = line[0] + year + '_postprocess/' + line[1:]
          if not any(i in line for i in ['LFV', 'Run1']):
            line += '  scale: ' + str(int(lumi)/137570.0) + '\n'
        if not skip_signal and not any(i in line for i in ['yields-group']): string_for_qcd += line


  with open(config_path + 'files_Run2.yml', 'a') as fnew:
    fnew.write(string_for_qcd)

  with open(config_path + 'template_Run2.yml') as f:
    lines = f.readlines()
    with open(config_path + 'config_Run2.yml', 'w+') as f1:
      for line in lines: f1.write(line)
      f1.write(common_syst)
      f1.write(file_syst)
      f1.write("\nplots:\n  include: ['histos_dnn.yml']\n")

  #call(['../plotIt/plotIt', '-o ' + dest_path + '/figures/qcd', config_path + 'config_Run2.yml'], shell=False)
