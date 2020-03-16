#################################################################################
# Classification.py                                                             #
#                                                                               #
# 1. Search data and MC NanoAOD samples at "/xrootd/store" (@ path_search.py)   #
# 2. Remove "/xrootd" in the path (@ path_search.py)                            #
# 3. Classify with Runs and Triggers (or Processes) (e.g. Run2017_SingleMuon)   #
# 4. Save classified paths into .txt files                                      #
# 5. Format the existing data and MC to DAS form                                #
#                                                                               #
#################################################################################


import path_search as ps    # Searching all of the NanoAOD Rootfiles.
import os, sys

def data_run(path):
    tmp = ''
    run = ['Run2016','Run2017','Run2018']
    for i in run:
        if i in path:
            tmp = i
    return tmp
            
def mc_run(path):
    tmp = ''
    run = ['RunIISummer16','RunIIFall17','RunIIAutumn18']
    for i in run:
        if i in path:
            tmp = i
    return tmp

def classification(input_list, data_or_mc):
    dic_class = {}
    for i in input_list:
        if data_or_mc == "data":
            a = data_run(i)
        elif data_or_mc == "mc":
            a = mc_run(i)
        b = i.split('/')[4]
        mode = a + "_" + b
        if mode not in dic_class:
            dic_class[mode] = []
        dic_class[mode].append(i)
    print(dic_class)
    return dic_class

data_dir = '/xrootd/store/data'
mc_dir = '/xrootd/store/mc'
if os.path.exists('List'):
    os.rmdir('List')
os.mkdir('List')


print("(1/6) Searching for the NanoAOD DATA in KISTI T3")
list_data = ps.search_data(data_dir)


print("(2/6) Searching for the NanoAOD MC in KISTI T3")
list_mc = ps.search_mc(mc_dir)


print("(3/6) Classifying and Saving the DATA NanoAOD ...")
data_classification = classification(list_data, "data")
for key, paths in data_classification.items():
    with open("./List/data_" + key + ".txt","w") as f:
        for path in paths:
            f.write(path + "\n")


print("(4/6) Classifying and Saving the MC NanoAOD ...")
mc_classification = classification(list_mc, "mc")
for key, paths in mc_classification.items():
    with open("./List/mc_" + key + ".txt","w") as f:
        for path in paths:
            f.write(path + "\n")


print("(5/6) DAS formmating for DATA ...")
with open("./List/DAS_data.txt","w") as f:
    das_data_list = ps.das_format(list_data)
    for i in das_data_list:
        f.write(i+"\n")


print("(6/6) DAS formmating for MC ...")
with open("./List/DAS_mc.txt","w") as f:
    das_mc_list = ps.das_format(list_mc)
    for i in das_mc_list:
        f.write(i+"\n")

print("Done")

