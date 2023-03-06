import os
import sys
import ROOT
from ROOT import *
import numpy as np
import argparse

base_path = './'
parser = argparse.ArgumentParser()
parser.add_argument('-L', '--label', dest='label', type=str, default="rerun_staug22")
args = parser.parse_args()
label = args.label
#labels = ['rerun_multi_Multiaug22','rerun_staug22', 'rerun_ttaug22']
# Set Runs
years = ['16pre', '16post', '17', '18']

# Set output folders
for year in years:
	if not os.path.exists(base_path + label + '/' + year + '_postprocess'):
	    os.makedirs(base_path + label + '/' + year + '_postprocess')

# Systematic Sources => All systematics in one file.
systs={'':'', 'puup':'puup', 'pudown':'pudown',
'btagup_hf':'btaghfup','btagdown_hf':'btaghfdown','btagup_lf':'btaglfup','btagdown_lf':'btaglfdown',
'btagup_hfstats1':'btaghfstats1up','btagdown_hfstats1':'btaghfstats1down',
'btagup_lfstats1':'btaglfstats1up','btagdown_lfstats1':'btaglfstats1down',
'btagup_hfstats2':'btaghfstats2up','btagdown_hfstats2':'btaghfstats2down',
'btagup_lfstats2':'btaglfstats2up','btagdown_lfstats2':'btaglfstats2down',
'btagup_cferr1':'btagcferr1up','btagdown_cferr1':'btagcferr1down',
'btagup_cferr2':'btagcferr2up','btagdown_cferr2':'btagcferr2down',
'up_jesAbsolute':'jesAbsoluteup','down_jesAbsolute':'jesAbsolutedown',
'up_jesAbsolute_year':'jesAbsoluteyearup','down_jesAbsolute_year':'jesAbsoluteyeardown',
'up_jesBBEC1':'jesBBEC1up','down_jesBBEC1':'jesBBEC1down',
'up_jesBBEC1_year':'jesBBEC1yearup','down_jesBBEC1_year':'jesBBEC1yeardown',
'up_jesEC2':'jesEC2up','down_jesEC2':'jesEC2down',
'up_jesEC2_year':'jesEC2yearup','down_jesEC2_year':'jesEC2yeardown',
'up_jesFlavorQCD':'jesFlavorQCDup','down_jesFlavorQCD':'jesFlavorQCDdown',
'up_jesRelativeBal':'jesRelativeBalup','down_jesRelativeBal':'jesRelativeBaldown',
'up_jesRelativeSample_year':'jesRelativeSampleyearup','down_jesRelativeSample_year':'jesRelativeSampleyeardown'}

#systs=['puup']
# Produce dictionary for file lists.

nom_path = base_path + label
if not os.path.exists(nom_path):
    print("Folder '{}' does not exists.".format(nom_path))
else:
    print("Start postprocessing for '{}'.".format(nom_path))

file_list = {}
for year in years:
    if "multi" in label: file_list[year] = [i.replace('.root','') for i in os.listdir(nom_path+'/'+year+'/preds/') if '.root' in i and '__' not in i]
    else: file_list[year] = [i.replace('.root','') for i in os.listdir(nom_path+'/'+year) if '.root' in i and '__' not in i]
print(file_list)

def collect_systhists(outfile, fname, hlists, syst, syst_, year):
    if 'Run' not in fname and syst != '':
        try:
          tmpf = TFile.Open(os.path.join(nom_path, year, fname + '__' + syst + '.root'), 'READ')
        except:
          print("No file: " + nom_path + year + fname+'.root')
          return
    else: tmpf = TFile.Open(os.path.join(nom_path, year, fname + '.root'), 'READ')
    for histname in hlists:
        if syst != '' and 'counter' in histname: continue
        tmpf.cd()
        tmphist = tmpf.Get(histname)
        if syst == '': newtmphist = tmphist.Clone(histname)
        else: newtmphist = tmphist.Clone(histname + '__' + syst_)
        newtmphist.Scale(1./get_bSFratio(tmpf))
        outfile.cd()
        newtmphist.Write()
    tmpf.Close()
    return

def get_bSFratio(infile):
    prehist = infile.Get('hnevents_pglep_cut0000')
    posthist = infile.Get('hnevents_cut0000')
    if prehist.Integral() * posthist.Integral() == 0:
        return 1
    return posthist.Integral() / prehist.Integral()

# Loop over all files.
for year in years:
    out_path = nom_path + '/' + year + '_postprocess'
    for fname in file_list[year]:
        if "multi" in label : infile = TFile.Open(os.path.join(nom_path, year, "preds", fname+'.root'), 'READ')
        else : infile = TFile.Open(os.path.join(nom_path, year, fname+'.root'), 'READ')
        hlists = [ h.GetName() for h in infile.GetListOfKeys() if any(i in h.GetName() for i in ['dnn_pred', 'counter']) ]
        # Get ratio for rescaling with b-tagSF.
        ratio = get_bSFratio(infile)
        outfname = fname.replace("_" + year + "_" + fname.split("_")[-1], "")
        if "Run" in fname:
            outfname = fname.replace("_" + fname.split("_")[-1], "")
        print("Saving histograms at {}/hist_{}.root".format(out_path, outfname))
        # Collecting Histograms in outfile.
        outfile = TFile.Open(os.path.join(out_path, "hist_" + outfname + '.root'), 'RECREATE')
        # Looping over all systematics.
        for syst, syst_ in systs.items():
            if "year" in syst:
              syst = syst.replace('year', year)
              syst_ = syst_.replace('year', year)
            if "multi" in label: collect_systhists(outfile, fname, hlists, syst, syst_, year+"/preds/")
            else: collect_systhists(outfile, fname, hlists, syst, syst_, year)
        outhlists = [ h.GetName() for h in outfile.GetListOfKeys() if 'cut' in h.GetName() ]
        for h in outhlists:
            if "Run" in fname:
                continue
            if h == "hcounter_nocut":
                newhist = outfile.Get(h)
                newhist.Write()
            if ('nobweight' in h) and ('hncleanbjetspass' not in h):
                continue
            if ('pred' in h):
                outfile.cd()
                newhist = outfile.Get(h)
                ratio = 1
                newhist.Scale(1/ratio)
                newhist.Write()
        infile.Close()
        outfile.Close()
