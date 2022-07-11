import os
import sys
import ROOT
from ROOT import *
import numpy as np

base_path = './'
label = 'mar_02'
if len(sys.argv) > 1:
    nom_path = base_path + label + '_norm'
if not os.path.exists(nom_path):
    print("Folder '{}' does not exists.".format(nom_path))
else:
    print("Start postprocessing at '{}'.".format(nom_path))

# Set Runs
runs = ['16pre', '16post', '17', '18']
#runs = ['18']

# Set output folders
out_path = base_path + label + '_postprocess'
if not os.path.exists(out_path):
    for run in runs:
        os.makedirs(out_path + '/' + run)

# Systematic Sources => All systematics in one file.
systs = ['jesup','jesdown','puup','pudown',
'btagup_hf','btagdown_hf','btagup_lf','btagdown_lf',
'btagup_hfstats1','btagdown_hfstats1',
'btagup_hfstats2','btagdown_hfstats2',
'btagup_lfstats1','btagdown_lfstats1',
'btagup_lfstats2','btagdown_lfstats2',
'btagup_cferr1','btagdown_cferr1',
'btagup_cferr2','btagdown_cferr2',]

# Produce dictionary for file lists.
file_list = {}
for run in runs:
    file_list[run] = [i.replace('.root','') for i in os.listdir(nom_path+'/'+run) if '.root' in i]

def collect_systhists(outfile,fname,hlists,syst):
    fname = fname.replace(fname.split('_')[-1],'')
    syst_path = base_path+label+'_'+syst
    tmpf = TFile.Open(os.path.join(syst_path,run,fname+syst+'.root'), 'READ')
    for histname in hlists:
        tmpf.cd()
        tmphist = tmpf.Get(histname)
        newsyst = syst
        if 'btag' in syst:
            if 'up' in syst:
                newsyst = 'btag_' + syst.split('_')[-1] + 'up'
            elif 'down' in syst:
                newsyst = 'btag_' + syst.split('_')[-1] + 'down'
        newtmphist = tmphist.Clone(histname + '__' + newsyst)
        outfile.cd()
        newtmphist.Write()
    tmpf.Close()
    return

def get_bSFratio(infile):
    prehist = infile.Get('hnevents_pglep_cut000')
    posthist = infile.Get('hnevents_cut000')
    if prehist.Integral() * posthist.Integral() == 0:
        return 1
    return posthist.Integral() / prehist.Integral()

# Loop over all files.
for run in runs:
    for fname in file_list[run]:
        #print(os.path.join(nom_path,run,fname))
        infile = TFile.Open(os.path.join(nom_path,run,fname+'.root'), 'READ')
        hlists = [ h.GetName() for h in infile.GetListOfKeys() if 'cut' in h.GetName() ]
        ratio = get_bSFratio(infile)
        outfname = fname.replace("_"+run+"_"+fname.split("_")[-1],"")
        print("Saving histograms at {}/{}/hist_{}.root".format(out_path,run,outfname))
        outfile = TFile.Open(os.path.join(out_path,run,"hist_"+outfname+'.root'), 'RECREATE')
        # Collecting Histograms
        for syst in systs:
            collect_systhists(outfile,fname,hlists,syst)
        outhlists = [ h.GetName() for h in outfile.GetListOfKeys() if 'cut' in h.GetName() ]
        for h in outhlists:
            if "Run" in fname:
                newhist = outfile.Get(h)
                outfile.cd()
                newhist.Write()
                continue
            if ('event' in h) or ('counter' in h):
                continue
            if h[:2] == 'h1':
                continue
            if 'cut0000' in h:
                outfile.cd()
                newhist = outfile.Get(h)
                newhist.Scale(ratio)
                newhist.Write()
        infile.Close()
        outfile.Close()
