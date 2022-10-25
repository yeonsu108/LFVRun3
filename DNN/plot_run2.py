import sys, os
import re
from subprocess import call

config_path = '../../plotIt/configs/'
common_syst = 'systematics:\n'
groups = ['GData', 'Gttll', 'Gttlj', 'Gttjj', 'GttV', 'GZJets', 'GWJets', 'GSingleT', 'GVV', 'GQCD',
          'GLFVSTcv', 'GLFVSTuv', 'GLFVTTcv', 'GLFVTTuv',]
#not include prefire and elzvtx which exist only in 2017
#common_syst_list = ['pu', 'muid', 'muiso', 'mutrg', 'elid', 'elreco', 'eltrg',
common_syst_list = ['pu', 'lf', 'hf', 'lfstat1', 'lfstat2', 'hfstat1', 'hfstat2', 'cferr1', 'cferr2']
syst = ["jecAbsoluteup","jecAbsolutedown", "jecAbsoluteERAup", "jecAbsoluteERAdown",
        "jecBBEC1up", "jecBBEC1down", "jecBBEC1ERAup", "jecBBEC1ERAdown",
        "jecFlavorQCDup", "jecFlavorQCDdown", "jecRelativeBalup", "jecRelativeBaldown",
        "jecRelativeSampleERAup", "jecRelativeSampleERAdown",
        "jerup","jerdown"]
syst = ['puup', 'pudown', 'btagup_hf', 'btagdown_hf', 'btagup_lf', 'btagdown_lf', 'btagup_hfstats1', 'btagdown_hfstats1', 'btagup_hfstats2', 'btagdown_hfstats2', 'btagup_lfstats1', 'btagdown_lfstats1', 'btagup_lfstats2', 'btagdown_lfstats2', 'btagup_cferr1', 'btagdown_cferr1', 'btagup_cferr2', 'btagdown_cferr2', 'up_jesAbsolute', 'down_jesAbsolute', 'up_jesBBEC1', 'down_jesBBEC1', 'up_jesEC2', 'down_jesEC2', 'up_jesFlavorQCD', 'down_jesFlavorQCD', 'up_jesRelativeBal', 'down_jesRelativeBal', 'up_jesAbsolute_year', 'down_jesAbsolute_year', 'up_jesBBEC1_year', 'down_jesBBEC1_year', 'up_jesEC2_year', 'down_jesEC2_year', 'up_jesRelativeSample_year', 'down_jesRelativeSample_year']
for sy in syst:
  if 'ERA' in sy:
    common_syst_list.append(sy.replace('ERA', '2016'))
    common_syst_list.append(sy.replace('ERA', '2017'))
    common_syst_list.append(sy.replace('ERA', '2018'))
  else: common_syst_list.append(sy)

reco_str = 'rerun_CHaug22'
ch = ['st', 'tt']

for i in ch:
  dest_path = reco_str.replace('CH', i)
  if not os.path.exists(dest_path + "/" + i):
    try: os.makedirs(dest_path + "/" + i)
    except: pass
  if not os.path.exists(dest_path + "/" + i + '/qcd'):
    try: os.makedirs(dest_path + "/" + i + '/qcd')
    except: pass

for item in common_syst_list:
  common_syst += '  - ' + item + '\n'

for scenario in reco_str:
  string_for_files = ''
  #Firstly, merge file list + scale
  with open(config_path + 'files_2017.yml') as f:
    lines = f.readlines()
    skip_signal = False
    for line in lines:
      if '#' in line[0]: line = line[1:]
      if skip_signal and 'hist' in line: skip_signal = False
      if 'TH1L3B' in line: skip_signal = True
      if 'hist_QCD' in line: skip_signal = True
      if 'hist' in line:
        line = line[0] + '2017/' + scenario + ver17 + '/post_process/' + line[1:]
        if not any(i in line for i in ['TH1L3B', 'Run201']):
          line += '  scale: ' + str(41529/101270.0) + '\n'
      if not skip_signal and not any(i in line for i in ['yields-group']):
        if 'group' in line and not any(i in line for i in groups): string_for_files += '  group: Gother \n'
        else: string_for_files += line

  with open(config_path + 'files_2018.yml') as f:
    lines = f.readlines()
    skip_signal = False
    for line in lines:
      if '#' in line[0]: line = line[1:]
      if skip_signal and 'hist' in line: skip_signal = False
      if 'TH1L3B' in line: skip_signal = True
      if 'hist_QCD' in line: skip_signal = True
      if 'hist' in line:
        line = line[0] + '2018/' + scenario + ver18 + '/post_process/' + line[1:]
        if not any(i in line for i in ['TH1L3B', 'Run201']):
          line += '  scale: ' + str(59741/101270.0) + '\n'
      if not skip_signal and not any(i in line for i in ['yields-group']):
        if 'group' in line and not any(i in line for i in groups): string_for_files += '  group: Gother \n'
        else: string_for_files += line

  with open(config_path + 'files_1718.yml', 'w+') as fnew:
    print>>fnew, """
'full1718/{0}/hist_STTH1L3BHct.root':
  type: signal
  pretty-name: 'STTH1L3BHct'
  cross-section: 0.076
  generated-events: 1000000
  group: GSTHct
  order: 1

'full1718/{0}/hist_TTTH1L3BHct.root':
  type: signal
  pretty-name: 'TTTH1L3BHct'
  cross-section: 1.86
  generated-events: 1000000
  group: GTTHct
  order: 2

'full1718/{0}/hist_STTH1L3BHut.root':
  type: signal
  pretty-name: 'STTH1L3BHut'
  cross-section: 0.55
  generated-events: 1000000
  group: GSTHut
  order: 3

'full1718/{0}/hist_TTTH1L3BHut.root':
  type: signal
  pretty-name: 'TTTH1L3BHut'
  cross-section: 1.86
  generated-events: 1000000
  group: GTTHut
  order: 4
    """.format(scenario)
    fnew.write(string_for_files)

  file_syst = ''
  with open(config_path + 'config_2017.yml') as f:
    lines = f.readlines()
    for line in lines:
      if 'type' in line:
        if 'const' in line:
          file_syst += line[:line.find(':')] + '_17' + line[line.find(':'):line.find('hist')] + '2017/' + scenario + ver17 + '/post_process/' + line[line.find('hist'):]
        elif 'shape' in line:
          file_syst += line[:line.find('hist')] + '2017/' + scenario + ver17 + '/post_process/' + line[line.find('hist'):]

  with open(config_path + 'config_2018.yml') as f:
    lines = f.readlines()
    for line in lines:
      if 'type' in line:
        if 'const' in line:
          file_syst += line[:line.find(':')] + '_18' + line[line.find(':'):line.find('hist')] + '2018/' + scenario + ver18 + '/post_process/' + line[line.find('hist'):]
        elif 'shape' in line:
          file_syst += line[:line.find('hist')] + '2018/' + scenario + ver18 + '/post_process/' + line[line.find('hist'):]

  with open(config_path + 'template_1718.yml') as f:
    lines = f.readlines()
    with open(config_path + 'config_1718.yml', 'w+') as f1:
      for line in lines: f1.write(line)
      f1.write(common_syst)
      f1.write(file_syst)
      #if scenario == 'STFCNC': f1.write("\nplots:\n  include: ['histos_control.yml', 'histos_" + scenario.lower() + ".yml']\n")
      #else: f1.write("\nplots:\n  include: ['histos_" + scenario.lower() + ".yml']\n")
      #f1.write("\nplots:\n  include: ['histos_" + scenario.lower() + "_paper.yml']\n")
      f1.write("\nplots:\n  include: ['histos_" + scenario.lower() + "_thesis.yml']\n")

  call(['../../plotIt/plotIt', '-o ' + dest_path + '/' + scenario, config_path + 'config_1718.yml'], shell=False)


  #For QCD
  string_for_qcd = ''
  with open(config_path + 'files_2017.yml') as f:
    lines = f.readlines()
    skip_signal = True
    for line in lines:
      if '#' in line[0]: line = line[1:]
      if skip_signal and 'hist_QCD' in line: skip_signal = False
      if 'hist_QCD' in line:
        line = line[0] + '2017/' + scenario + ver17 + '/post_process/' + line[1:]
        if not any(i in line for i in ['TH1L3B', 'Run201']):
          line += '  scale: ' + str(41529/101270.0) + '\n'
      if not skip_signal and not any(i in line for i in ['yields-group']): string_for_qcd += line

  with open(config_path + 'files_2018.yml') as f:
    lines = f.readlines()
    skip_signal = True
    for line in lines:
      if '#' in line[0]: line = line[1:]
      if skip_signal and 'hist_QCD' in line: skip_signal = False
      if 'hist_QCD' in line:
        line = line[0] + '2018/' + scenario + ver18 + '/post_process/' + line[1:]
        if not any(i in line for i in ['TH1L3B', 'Run201']):
          line += '  scale: ' + str(59741/101270.0) + '\n'
      if not skip_signal and not any(i in line for i in ['yields-group']): string_for_qcd += line

  with open(config_path + 'files_1718.yml', 'a') as fnew:
    fnew.write(string_for_qcd)

  with open(config_path + 'template_1718.yml') as f:
    lines = f.readlines()
    with open(config_path + 'config_1718.yml', 'w+') as f1:
      for line in lines: f1.write(line)
      f1.write(common_syst)
      f1.write(file_syst)
      #if scenario == 'STFCNC': f1.write("\nplots:\n  include: ['histos_control_qcd.yml', 'histos_" + scenario.lower() + "_qcd.yml']\n")
      #else: f1.write("\nplots:\n  include: ['histos_" + scenario.lower() + "_qcd.yml']\n")
      #f1.write("\nplots:\n  include: ['histos_" + scenario.lower() + "_qcd_paper.yml']\n")
      f1.write("\nplots:\n  include: ['histos_" + scenario.lower() + "_thesis.yml']\n")

  if scenario == 'STFCNC':
    call(['../../plotIt/plotIt', '-o ' + dest_path + '/' + scenario + '/qcd', config_path + 'config_1718.yml'], shell=False)
