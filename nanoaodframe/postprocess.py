import os
import sys
import ROOT
from ROOT import *
import numpy as np

base_path = './'
label = 'aug22_stlfv'
nom_path = base_path + label + '/nom/'
if not os.path.exists(nom_path):
    print("Folder '{}' does not exists.".format(nom_path))
else:
    print("Start postprocessing at '{}'.".format(nom_path))

# Set Runs
runs = ['16pre', '16post', '17', '18']
#runs = ['18']

# Set output folders
out_path = base_path + label + '/postprocess'
if not os.path.exists(out_path):
    for run in runs:
        os.makedirs(out_path + '/' + run)

# Systematic Sources => All systematics in one file.
systs = ['nom','puup','pudown',
'btagup_hf','btagdown_hf','btagup_lf','btagdown_lf',
'btagup_hfstats1','btagdown_hfstats1',
'btagup_hfstats2','btagdown_hfstats2',
'btagup_lfstats1','btagdown_lfstats1',
'btagup_lfstats2','btagdown_lfstats2',
'btagup_cferr1','btagdown_cferr1',
'btagup_cferr2','btagdown_cferr2',
'up_jesAbsolute','down_jesAbsolute',
]

systs=['nom','puup','pudown',
'btagup_hf','btagdown_hf','btagup_lf','btagdown_lf',
'btagup_hfstats1','btagdown_hfstats1','btagup_lfstats1','btagdown_lfstats1',
'btagup_hfstats2','btagdown_hfstats2','btagup_lfstats2','btagdown_lfstats2',
'btagup_cferr1','btagdown_cferr1','btagup_cferr2','btagdown_cferr2',
'up_jesAbsolute','down_jesAbsolute','up_jesAbsolute_year','down_jesAbsolute_year',
'up_jesBBEC1','down_jesBBEC1','up_jesBBEC1_year','down_jesBBEC1_year',
'up_jesEC2','down_jesEC2','up_jesEC2_year','down_jesEC2_year',
'up_jesFlavorQCD','down_jesFlavorQCD','up_jesRelativeBal','down_jesRelativeBal',]

#systs=['puup']
# Produce dictionary for file lists.
file_list = {}
for run in runs:
    file_list[run] = [i.replace('.root','') for i in os.listdir(nom_path+'/'+run) if '.root' in i]

def collect_systhists(outfile,fname,hlists,syst,run):
    fname = fname.replace(fname.split('_')[-1],'')
    syst_path = base_path+label+'/'+syst
    tmpf = TFile.Open(os.path.join(syst_path,run,fname+syst+'.root'), 'READ')
    for histname in hlists:
        tmpf.cd()
        tmphist = tmpf.Get(histname)
        if (syst == "nom") or ("Run" in fname):
            newtmphist = tmphist
        else:
            newsyst = syst
            if 'btag' in syst:
                if 'up' in syst:
                    newsyst = 'btag_' + syst.split('_')[-1] + 'up'
                elif 'down' in syst:
                    newsyst = 'btag_' + syst.split('_')[-1] + 'down'
            if 'jes' in syst:
                if 'up' in syst:
                    newsyst = syst.replace('up_','') + 'up'
                elif 'down' in syst:
                    newsyst = syst.replace('down_','') + 'down' 
            if 'year' in syst:
                if '16' in run:
                    newsyst = syst.replace('year','2016')
                elif '17' in run:
                    newsyst = syst.replace('year','2017')
                elif '18' in run:
                    newsyst = syst.replace('year','2018')
            newtmphist = tmphist.Clone(histname + '__' + newsyst)
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
for run in runs:
    for fname in file_list[run]:
        #print(os.path.join(nom_path,run,fname))
        infile = TFile.Open(os.path.join(nom_path,run,fname+'.root'), 'READ')
        hlists = [ h.GetName() for h in infile.GetListOfKeys() if 'cut' in h.GetName() ]
        # Get ratio for rescaling with b-tagSF.
        ratio = get_bSFratio(infile)
        outfname = fname.replace("_"+run+"_"+fname.split("_")[-1],"")
        if "Run" in fname:
            outfname = fname.replace("_"+fname.split("_")[-1],"")
        print("Saving histograms at {}/{}/hist_{}.root".format(out_path,run,outfname))
        # Collecting Histograms in outfile.
        outfile = TFile.Open(os.path.join(out_path,run,"hist_"+outfname+'.root'), 'RECREATE')
        # Looping over all systematics.
        for syst in systs:
            if ("Run" in fname) and (syst != "nom"): continue  # Skip DATA
            collect_systhists(outfile,fname,hlists,syst,run)
        outhlists = [ h.GetName() for h in outfile.GetListOfKeys() if 'cut' in h.GetName() ]
        for h in outhlists:
            if "Run" in fname:
                continue
            if ('event' in h) or ('counter' in h):
                continue
            if ('nobweight' in h) and ('hncleanbjetspass' not in h):
                continue
            if ('cut00000' in h) or ('hncleanbjetspass' in h):
                outfile.cd()
                newhist = outfile.Get(h)
                ratio = 1
                newhist.Scale(1/ratio)
                newhist.Write()
        infile.Close()
        outfile.Close()
