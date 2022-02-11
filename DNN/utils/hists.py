import uproot
import numpy as np
import matplotlib as plt

def hists(tree,pred,weight):
    hists = []
    keys = []
    hists.append(np.histogram(pred,20,(0.0,1.0),weight,density=False))
    keys.append("dnn")
    return zip(keys, hists)
