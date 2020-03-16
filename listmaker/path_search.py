import os, sys

def xrootd_form(total_path):
    xrd_path = 'root://cms-xrdr.sdfarm.kr:1094//xrd'
    path = total_path.replace('/xrootd',xrd_path)
    return path

def search_data(data_dir): 
    list_data = []
    for i, (path, dir, files) in enumerate(os.walk(data_dir)):
        if "NANOAOD" not in path:
            continue
        elif "25Oct2019" not in path:
            continue
        else:
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == ".root":
                    p = path.replace("/xrootd","")
                    x = p + "/" + filename
                    list_data.append(x)
    return list_data


def search_mc(mc_dir):
    list_mc = []
    for i, (path, dir, files) in enumerate(os.walk(mc_dir)):
        if "NanoAODv6" not in path:
            continue
        elif "25Oct2019" not in path:
            continue
        else:
            for filename in files:
                ext = os.path.splitext(filename)[-1]
                if ext == ".root":
                    p = path.replace("/xrootd","")
                    x = p + "/" + filename
                    list_mc.append(x)
    return list_mc


def das_format(path_list):
    tmp = 'tmp'
    das_list = []
    for path in path_list:
        seg_name = path.split("/")
        das_name = "/" + seg_name[4] + "/" +seg_name[3] + "-" + seg_name[6] + "/" + seg_name[5]
        if tmp == das_name:
            continue
        tmp = das_name
        das_list.append(das_name)
    return das_list
