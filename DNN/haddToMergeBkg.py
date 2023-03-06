import ROOT
import sys, os
from subprocess import check_call
from os import listdir, path
import collections
import glob
import subprocess

dir_path_st = "/home/itseyes/github/LFVRun2_ndf_integration/nanoaodframe/aug22_stlfv/"
dirs_st = os.listdir(dir_path_st)

dir_path_tt = "/home/itseyes/github/LFVRun2_ndf_integration/nanoaodframe/aug22_ttlfv/"
dirs_tt = os.listdir(dir_path_tt)

dir_path_merged = "/data1/users/ecasilar/processed_LFV/aug22_mergedlfv/"

for dsyst in os.listdir(dir_path_st):
	for year in os.listdir(dir_path_st+"/"+dsyst):
		if ".root" in year: continue
		if not os.path.exists(dir_path_merged+"/"+dsyst+"/"+year):
		  try: os.makedirs(dir_path_merged+"/"+dsyst+"/"+year)
		  except: pass
		for rfile in os.listdir(dir_path_st+"/"+dsyst+"/"+year): 
			if not ".root" in rfile: continue
			if "LFV" in rfile: continue
			print(rfile)	
			print(['hadd','-f', dir_path_merged+'/'+dsyst+'/'+year+'/' + rfile] + [dir_path_st+'/'+dsyst+'/'+year+'/' + rfile] + [dir_path_tt+'/'+dsyst+'/'+year+'/' + rfile])
			subprocess.run(['hadd','-f', dir_path_merged+'/'+dsyst+'/'+year+'/' + rfile] + [dir_path_st+'/'+dsyst+'/'+year+'/' + rfile] + [dir_path_tt+'/'+dsyst+'/'+year+'/' + rfile])
