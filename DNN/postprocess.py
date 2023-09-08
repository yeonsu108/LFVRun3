import os, sys, glob
import ROOT
from ROOT import *
import numpy as np
import subprocess
import argparse


base_path = './'
parser = argparse.ArgumentParser()
parser.add_argument('-L', '--label', dest='label', type=str, default="top_lfv_multiClass_jan03")
parser.add_argument('-D', '--discriminator', dest='discriminator', type=str, default="p_st_tt_ob")
parser.add_argument('-A', '--alpha', dest='alpha', type=str, default="0p1")
parser.add_argument('-Y', '--year', dest='year', type=str, default="2017")
args = parser.parse_args()
label = args.label
discriminator = args.discriminator
alpha = args.alpha
year = args.year


if year not in ['2016pre', '2016post', '2017', '2018']:
    print('Wrong year, check again')
    sys.exit()

yield_name = 'h_ncleanjetspass'
base_path = './'
nom_path = base_path+label

if not os.path.exists(nom_path):
    print("Folder '{}' does not exists.".format(nom_path))
    sys.exit()
else:
    print("Start postprocessing at '{}'.".format(nom_path))


out_path = nom_path + '/' + year + '_postprocess/' + discriminator + '/' + alpha + '/'
if not os.path.exists(base_path + label + '/' + year + '_postprocess/' + discriminator + '/' + alpha + '/'):
    os.makedirs(base_path + label + '/' + year + '_postprocess/' + discriminator + '/' + alpha + '/')


# Set output folders

file_list = [i.replace('.root', '') for i in os.listdir(nom_path+'/'+year+'/preds/'+discriminator+'/'+alpha +'/') if '.root' in i]
data_list = [i[:i.find('201')] for i in os.listdir(nom_path+'/'+year+'/preds/'+discriminator+'/'+alpha +'/') if '.root' in i and '201' in i and 'jes' not in i]
data_list = list(set(data_list))
#print(data_list)
#print(file_list)


def get_bSFratio(inputf, inputh):
    # ref: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BTagShapeCalibration
    # rescale histogram by Sum(event weights before applying b weight)/Sum(weights with b weight)
    # This should be done per jet bin - nojet / 3jet

    step = 'S4'
    if isFFcalc: step = 'S2'

    posthist = inputf.Get('h_nevents_' + step)
    prehist = inputf.Get('h_nevents_' + step + '_nobtag')
    if '__btag' in inputh:
        posthist = inputf.Get('h_nevents_' + step + '__' + str(inputh.split('__')[-1]))
    if prehist.Integral() * posthist.Integral() == 0:
        return 1.0
    #print(prehist.Integral() / posthist.Integral())
    return prehist.Integral(0, prehist.GetNbinsX()+1) / posthist.Integral(0, prehist.GetNbinsX()+1)


def get_Scale(inputf):

    nom_sumW=inputf.Get('hcounter_nom')
    sumW=inputf.Get('hcounter')
    return float(nom_sumW.Integral(0, nom_sumW.GetNbinsX()+1) / sumW.Integral(0,sumW.GetNbinsX()+1))

# Loop over all files.
for fname in file_list:
    #print(os.path.join(nom_path, fname))
    #if not any(i in fname for i in ['TTToSemiLeptonic']): continue
    #if not 'tuneup' in fname: continue
    infile = TFile.Open(os.path.join(nom_path+'/'+year+'/preds/'+discriminator+'/'+alpha +'/', fname + '.root'), 'READ')
    hlists = [ h.GetName() for h in infile.GetListOfKeys() if '_S' in h.GetName() or 'dnn' in h.GetName()]
    hlists.append("hcounter")
    print("HLIST", hlists)

    # Get ratio for rescaling with b-tagSF.
    if not '__' in fname: bSFfile = infile
    elif '__' in fname and any(i in fname for i in [ 'jes']):
        bSFfile = infile
    else:
        bSFfname = fname.replace('__' + fname.split('__')[1], '')
        bSFfile = TFile.Open(os.path.join(nom_path+'/'+year+'/preds/'+discriminator+'/'+alpha +'/', bSFfname + '.root'), 'READ')

    if 'TTT' in fname:
       if any(i in fname for i in ['hdamp', 'tune']):
          print("Trying to read file :", bSFfile)
          nom_sumW=infile.Get('hcounter_nom')
          sumW=infile.Get('hcounter')
          scale_for_norm = float(nom_sumW.Integral(0, nom_sumW.GetNbinsX()+1) / sumW.Integral(0,sumW.GetNbinsX()+1))
          print("SCALE : ", scale_for_norm)

    # Collecting Histograms in outfile.
    print("Saving histograms at {}/{}.root".format(out_path, fname))
    outfile = TFile.Open(os.path.join(out_path, fname+'.root'), 'RECREATE')


    nominal_list = []

    for hname in hlists:
        print("HISTO : ", hname)
        if "__" not in hname: nominal_list.append(hname)
        h = infile.Get(hname)
        if any(i in hname for i in ['event', 'counter', '_nobtag', 'LHEPdfWeightSum']): pass
        elif any(i in hname for i in ['__scale', '__ps', '__pdf']): continue
        elif 'SingleMuon' in fname and 'jes' not in fname: pass
        else:
            print("FNAME to be scaled :" , fname)
            ratio = get_bSFratio(bSFfile, hname)
            h.Scale(ratio)
        if 'TTT' in fname:
           if any(i in fname for i in ['hdamp', 'tune']):
              h.Scale(scale_for_norm)
        h.Write()

    hcounter = infile.Get('hcounter')
    nominal_list = list(set(nominal_list))

    infile.Close()
    outfile.Close()


for dataname in data_list:
    try:
        subprocess.call(['rm', os.path.join(out_path, dataname + year + '.root')])
    except: pass
    subprocess.check_call( ["hadd", "-f", os.path.join(out_path, dataname + year + '.root')] + glob.glob(os.path.join(out_path, dataname) + '201*') )
