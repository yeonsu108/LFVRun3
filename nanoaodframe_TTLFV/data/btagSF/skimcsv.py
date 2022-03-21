import pandas as pd

infile = 'reshaping_deepJet_106XUL16preVFP_v2.csv'
df = pd.read_csv(infile)
# Central, JES, HF, LF, (HF/LF)Stats(1/2)
systs = ['central','up_jes','down_jes','up_hf','down_hf','up_lf',
        'down_lf','up_hfstats1','down_hfstats1','up_hfstats2','down_hfstats2',
        'up_lfstats1','down_lfstats1','up_lfstats2','down_lfstats2']

skimdf = df.loc[df['sysType'].isin(systs)]
print(skimdf)

skimdf.to_csv('skimmed_'+infile)
