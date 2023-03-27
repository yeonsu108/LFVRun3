import os
import sys
import ROOT
from ROOT import *
import numpy as np
import argparse

base_path = './'
parser = argparse.ArgumentParser()
parser.add_argument('-L', '--label', dest='label', type=str, default="rerun_staug22")
parser.add_argument('-D', '--discriminator', dest='discriminator', type=str, default="p_st_tt_ob")
parser.add_argument('-A', '--alpha', dest='alpha', type=str, default="1p0")
args = parser.parse_args()
label = args.label
discriminator = args.discriminator
alpha = args.alpha
#labels = ['rerun_multi_Multiaug22','rerun_staug22', 'rerun_ttaug22']
# Set Runs
years = ['2016pre', '2016post', '2017','2018']
#years = [ '2018']

# Set output folders
for year in years:
	if not os.path.exists(base_path + label + '/' + year + '_postprocess/' + discriminator + '/' + alpha + '/'):
	    os.makedirs(base_path + label + '/' + year + '_postprocess/' + discriminator + '/' + alpha + '/')

# Systematic Sources => All systematics in one file.

systs_tofile = ['jerdown', 'jerup', 'jesAbsolute_yeardown', 'jesAbsolute_yearup', 'jesAbsolutedown', 'jesAbsoluteup', 'jesBBEC1_yeardown', 'jesBBEC1_yearup', 'jesBBEC1down', 'jesBBEC1up', 'jesFlavorQCDdown', 'jesFlavorQCDup', 'jesRelativeBaldown', 'jesRelativeBalup', 'jesRelativeSample_yeardown', 'jesRelativeSample_yearup', 'tesdown', 'tesup']
systs_toweight = ['btagcferr1down', 'btagcferr1up', 'btagcferr2down', 'btagcferr2up', 'btaghfdown', 'btaghfstats1down', 'btaghfstats1up', 'btaghfstats2down', 'btaghfstats2up', 'btaghfup', 'btaglfdown', 'btaglfstats1down', 'btaglfstats1up', 'btaglfstats2down', 'btaglfstats2up', 'btaglfup', 'muiddown', 'muidup', 'muisodown', 'muisoup', 'mutrgdown', 'mutrgup', 'pudown', 'puup', 'tauideldown', 'tauidelup', 'tauidjetdown', 'tauidjetup', 'tauidmudown', 'tauidmuup']
systs = systs_tofile+systs_toweight+['']

# Produce dictionary for file lists.

nom_path = base_path + label
if not os.path.exists(nom_path):
    print("Folder '{}' does not exists.".format(nom_path))
else:
    print("Start postprocessing for '{}'.".format(nom_path))

file_list = {}
print(os.listdir(nom_path+'/'+year+'/preds/'+discriminator+'/'+alpha +'/'))
for year in years:
    if "multi" in label.lower(): file_list[year] = [i.replace('.root','') for i in os.listdir(nom_path+'/'+year+'/preds/'+discriminator+'/'+alpha +'/') if '.root' in i and '__' not in i]
    else: file_list[year] = [i.replace('.root','') for i in os.listdir(nom_path+'/'+year) if '.root' in i and '__' not in i]
print(file_list)

def collect_systhists(outfile, fname, hlists, syst, syst_, year):
    if 'SingleMuon' not in fname and syst != '':
        try:
          tmpf = TFile.Open(os.path.join(nom_path, year, fname + '__' + syst.replace("year",year[:4]) + '.root'), 'READ')
        except:
          print("No file: " + os.path.join(nom_path, year, fname + '__' + syst.replace("year",year[:4]) + '.root'))
          return
    else: tmpf = TFile.Open(os.path.join(nom_path, year, fname + '.root'), 'READ')
    for histname in hlists:
        if syst != '' and 'counter' in histname: continue
        tmpf.cd()
        tmphist = tmpf.Get(histname)
        if syst == '': newtmphist = tmphist.Clone(histname)
        else: newtmphist = tmphist.Clone(histname + '__' + syst_)
        if 'SingleMuon' not in fname: newtmphist.Scale(1./get_bSFratio(tmpf))
        else: newtmphist.Scale(1.)
        outfile.cd()
        newtmphist.Write()
    tmpf.Close()
    return

def get_bSFratio(infile):
    prehist = infile.Get('h_nevents_S5_nobtag')
    posthist = infile.Get('h_nevents_S5')
    if prehist.Integral() * posthist.Integral() == 0:
        return 1
    else :
        return posthist.Integral() / prehist.Integral()

# Loop over all files.
for year in years:
    out_path = nom_path + '/' + year + '_postprocess/' + discriminator + '/' + alpha + '/'
    for fname in file_list[year]:
        if "multi" in label.lower() : infile = TFile.Open(os.path.join(nom_path, year, "preds",discriminator , alpha , fname+'.root'), 'READ')
        else : infile = TFile.Open(os.path.join(nom_path, year, fname+'.root'), 'READ')
        hlists = [ h.GetName() for h in infile.GetListOfKeys() if any(i in h.GetName() for i in ['dnn_pred', 'counter']) ]
        # Get ratio for rescaling with b-tagSF.
        if 'SingleMuon' not in fname: ratio = get_bSFratio(infile)
        else : ratio = 1
        outfname = fname.replace("_" + year + "_" + fname.split("_")[-1], "")
        if "SingleMuon" in fname:
            outfname = fname.replace("_" + fname.split("_")[-1], "")
        print("Saving histograms at {}/{}.root".format(out_path, outfname))
        # Collecting Histograms in outfile.
        outfile = TFile.Open(os.path.join(out_path, outfname + '.root'), 'RECREATE')
        # Looping over all systematics.
        #for syst, syst_ in systs.items():
        for syst in systs:
            if "year" in syst:
              syst = syst.replace('year', year[:4])
            syst_ = syst
            if "multi" in label.lower(): collect_systhists(outfile, fname, hlists, syst, syst_, year+"/preds/"+discriminator+"/"+alpha+"/")
            else: collect_systhists(outfile, fname, hlists, syst, syst_, year)
        outhlists = [ h.GetName() for h in outfile.GetListOfKeys() if 'cut' in h.GetName() ]
        for h in outhlists:
            print(h)
            if "SingleMuon" in fname:
                continue
            if h == "hcounter":
                newhist = outfile.Get(h)
                newhist.Write()
            if ('_nobtag' in h):
                continue
            if ('pred' in h):
                outfile.cd()
                newhist = outfile.Get(h)
                ratio = 1
                newhist.Scale(1/ratio)
                newhist.Write()
        infile.Close()
        outfile.Close()
