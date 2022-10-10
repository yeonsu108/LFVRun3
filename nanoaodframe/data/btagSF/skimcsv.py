import pandas as pd
pd.set_option('mode.chained_assignment',  None)
#infiles = ['reshaping_deepJet_106XUL16postVFP_v3.csv','reshaping_deepJet_106XUL16preVFP_v2.csv',
#        'reshaping_deepJet_106XUL17_v3.csv','reshaping_deepJet_106XUL18_v2.csv']

infiles = [ 'reshaping_deepJet_16postVFP.csv',
            'reshaping_deepJet_16preVFP.csv',
            'reshaping_deepJet_17.csv',
            'reshaping_deepJet_18.csv',
            ]

for infile in infiles:
    print(infile)
    df = pd.read_csv('update/'+infile)
    # Btag SF uncertainty sources without JES related.
    syst_types = ['hf','lf','hfstats1','hfstats2','lfstats1','lfstats2','cferr1','cferr2']
    # Btag SF uncertainty sources related with JES.
    jessyst_types = ['Absolute', 'Absolute_year', 'BBEC1', 'BBEC1_year', 'EC2', 'EC2_year', 'FlavorQCD', 'HF', 'HF_year', 'RelativeBal', 'RelativeSample_year']
    
    for syst in syst_types:
        print(syst)
        savelists = ['central']
        savelists.append('up_'+syst)
        savelists.append('down_'+syst)
        newdf = df.loc[df['sysType'].isin(savelists)]
        newdf.loc[df['OperatingPoint'] == 'shape','OperatingPoint'] = 3
        newdf.to_csv('update/skimmed_btag_'+syst+'_'+infile,index=False)
    
    for jessyst in jessyst_types:
        print(jessyst)
        savelists = ['central']
        if "year" in jessyst:
            year = "2018"
            if "16" in infile:      year = "2016"
            elif "17" in infile:    year = "2017"
            else:                   year = "2018"
            jessyst = jessyst.replace('year',str(year))
        savelists.append('up_jes'+jessyst)
        savelists.append('down_jes'+jessyst)
        newjesdf = df.loc[df['sysType'].isin(savelists)]
        newjesdf.loc[df['OperatingPoint'] == 'shape','OperatingPoint'] = 3
        newjesdf.to_csv('update/skimmed_btag_jes'+jessyst+'_'+infile,index=False)

