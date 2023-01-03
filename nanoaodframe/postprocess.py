import os, sys, glob
import ROOT
from ROOT import *
import numpy as np
import subprocess

label = sys.argv[1]
year = sys.argv[2]
if year not in ['2016pre', '2016post', '2017', '2018']:
    print('Wrong year, check again')
    sys.exit()

base_path = './'
nom_path = os.path.join(base_path, label, year)
if not os.path.exists(nom_path):
    print("Folder '{}' does not exists.".format(nom_path))
    sys.exit()
else:
    print("Start postprocessing at '{}'.".format(nom_path))


# Set output folders
out_path = os.path.join(base_path, label, year + '_postprocess')
if not os.path.exists(out_path):
    os.makedirs(out_path)

file_list = [i.replace('.root', '') for i in os.listdir(nom_path) if '.root' in i]
data_list = [i[:i.find('201')] for i in os.listdir(nom_path) if '.root' in i and '201' in i and 'jes' not in i]
data_list = list(set(data_list))
print(data_list)

def get_bSFratio(inputf, inputh):
    # ref: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagShapeCalibration
    # rescale histogram by Sum(event weights before applying b weight)/Sum(weights with b weight)
    # This should be done per jet bin - nojet / 3jet

    step = inputh[inputh.rfind('_S')+1:inputh.rfind('_S')+3]

    # This depends on cutflow
    if int(step[-1]) < 4: step = 'S' + step[-1]
    else                : step = 'S4'

    posthist = inputf.Get('h_nevents_' + step)
    prehist = inputf.Get('h_nevents_' + step + '__nobtag')
    if '__btag' in inputh:
        posthist = inputf.Get('h_nevents_' + step + '__' + str(inputh.split('__')[-1]))
    if prehist.Integral() * posthist.Integral() == 0:
        return 1.0
    #print(prehist.Integral() / posthist.Integral())
    return prehist.Integral() / posthist.Integral()


# Loop over all files.
for fname in file_list:
    #print(os.path.join(nom_path, fname))
    #if not any(i in fname for i in ['TTTo2L2Nu', 'TTToSemiLeptonic']): continue
    infile = TFile.Open(os.path.join(nom_path, fname + '.root'), 'READ')
    hlists = [ h.GetName() for h in infile.GetListOfKeys() if '_S' in h.GetName() ]
    hlists.append("hcounter")

    # Get ratio for rescaling with b-tagSF.
    if not '__' in fname: bSFfile = infile
    elif '__' in fname and any(i in fname for i in ['hdamp', 'tune']):
        bSFfile = infile
    else:
        bSFfname = fname.replace('__' + fname.split('__')[1], '')
        bSFfile = TFile.Open(os.path.join(nom_path, bSFfname + '.root'), 'READ')

    # Collecting Histograms in outfile.
    print("Saving histograms at {}/{}.root".format(out_path, fname))
    outfile = TFile.Open(os.path.join(out_path, fname+'.root'), 'RECREATE')

    for hname in hlists:
        h = infile.Get(hname)
        if any(i in hname for i in ['event', 'counter', '__nobtag', 'LHEPdfWeightSum']): pass
        elif '201' in fname and 'jes' not in fname: pass
        else:
            ratio = get_bSFratio(bSFfile, hname)
            h.Scale(ratio)
        h.Write()

        if 'ncleanjetspass' in hname:
            h1 = h.Clone('h1')
            h1.SetName(hname.replace('h_ncleanjetspass', 'h_ncleanjetspass_yield'))
            h1.Write()
    infile.Close()
    outfile.Close()


for dataname in data_list:
    try:
        subprocess.call(['rm', os.path.join(out_path, dataname + year + '.root')])
    except: pass
    subprocess.check_call( ["hadd", "-f", os.path.join(out_path, dataname + year + '.root')] + glob.glob(os.path.join(out_path, dataname) + '201*') )
