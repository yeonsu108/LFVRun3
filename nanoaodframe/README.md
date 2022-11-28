# NanoAOD RDataFrame

With this package, we can do the following to NanoAOD files
- Apply good JSON
- Calculate b-tag weights for MC
- Apply Jet/MET corrections
- Skim events
- Process events with applying selections
- SF and uncertainty calculation

For this, we use the data frame concept to simplify the code,
but it requires to learn new way of using ROOT.
In a data frame concept, the operations on data should be defined in terms of functions,
which means that result of applying a function should produce outputs and no internal states are allowed.
In ROOT, RDataFrame allows us to borrow the concept for analysis.

This package code implements LFV analysis using NanoAOD format.


## I. Introduction

- The advantage of using RDataFrame is that you don't have to
worry about looping, filling of histograms at the right place,
writing out trees. In some sense you can concentrate more on thinking about data analysis.

- Draw back is that you have to think of a new way of doing old things.
This could getting used to. Also complicated algorithms may not
be so easy to implement with RDataFrame

- Purely data frame concept is not ideal for HEP data since
we have to treat real data and simulated data differently.
We must apply different operations depending on the input data, such as scale factors and corrections.
Therefore, some form of global state should be stored. 
In this package, the data frame concept is used together with object oriented concept for this purpose.


## II. Code

- The code consists of a main class NanoAODAnalyzerrdframe. 
There is one header file `.h` and one source file `.cpp` for it.
The class has several methods:
    - Object definitions. `selectElectrons()`, `selectMuons()`, ...
    - Additional derived variables definition. `defineMoreVars()`
    - Histogram definitions. `bookHists()`
    - Selections. `defineCuts()`
    - Plus some utility methods/functions. `gen4vec()`, `readjson()`, `removeOverlaps()`, `helper_1DHistCreator()`, `createHists()`

- **Users should modify**: object definitions, define additional variables, histogram definitions, selections.

- To use the class, you need to pass a pointer to TChain object, output root file name and a JSON file.
  If there is `"genWeight"` branch in the ROOT Tree then the input is assumed to be MC, otherwise data.
  Look at `nanoaoddataframe.cpp` to find how to use within C++.

- Compile
  ``` bash
    make clean && make -j 4   # max 6 effective.
    ```
    Need ROOT 6.26.06 or later then for correctionlib,
    this will compile and create a `libnanoaodrdframe.so` shared library that can be loaded in a ROOT session or macro:
    ```c++
    gSystem->Load("libnanoadrdframe.so");
    ```
    or within pyROOT (look in `processnanoaod.py`).


## III. Running over large dataset

### Usage of scripts
In the `scripts/` folder, there are scripts for skimming or processing the NanoAOD files.
All of the options are set in the script files `scripts/*.sh`.

#### Skim
```bash
# You are at LFVRun2/nanoaodframe/
# First fetch dataset info from google spreadsheet:
# https://docs.google.com/spreadsheets/d/1KNvsRvXi3sgU45T2qOUztFSX3As4elZB325WaPnSkA8/edit#gid=569299692
# The argument will be the name of campaign in 'Campaign Summary' tab
# This will create file lists in data/dataset

python getDatasetInfo.py v8UL_2016pre

# Now, run script submitting slurm job
# arguments: folder, year (2016pre, 2016post, 2017, and 2018)
# You can add data or mc flag at the end of command if needed

python scripts/skim.py skim_test 2016pre

OR
python scripts/skim.py skim_test 2016pre data (mc)

# To run specific datasets, add them in test_list of skim.py
# This script uses slurm on htop.
# Please specify which node to EXCLUDE from the batch job, in scripts/job_slurm_skim.sh
```

#### Processing
`processnanoaod.py` scripts can automatically run over all ROOT files in an input directory.
``` txt
Usage: processnanoaod.py [options] inputDir outputDir

Options:
  -I, --indir           Input directory containing root files
  -O, --outdir          Output directory and file name 
  -h, --help            show this help message and exit
  -Y YEAR, --year=YEAR  Select 2016, 2017, or 2018 runs
  -S SYST, --syst=SYST  Systematic sources
  -J JSON, --json=JSON  Select events using this JSON file, meaningful only
                        for data
  --split=SPLIT         How many jobs to split into
  --skipold             Skip existing root files
  --recursive           Process files in the subdirectories recursively
  -A, --allinone        Process all files and output a single root file. You
                        must make sure MC and Data are not mixed together.
  --saveallbranches     Save all branches. False by default
  --globaltag=GLOBALTAG
                        Global tag to be used in JetMET corrections
```
  
By default, it will go into subdirectories recursively and process ROOT files. 
It will make the output directory to have the same  the directory structure as the input directory.
It will create one output file per one input file, so there is one-to-one correspondence.

`--split` option will allow multithreading you to use multiple CPUs to process the files. (e.g. `--split=5`)\
`--skipold` option will let you skip files that were analyzed, by matching files that have _analyzed in the file names.\
`--recursive` mode is on by default. If you don't want that, `--recursive=False`.\
`--allinone` option will let you get a single output root file for all the files in the inputDir. In this mode, `--skipold` doesn't work

### Usage of scripts
In the `scripts/` folder, there are scripts for skimming or processing the NanoAOD files.
All of the options are set in the script files `scripts/*.sh`.

#### Process
```bash
# You are at LFVRun2/nanoaodframe/
source ./scripts/processdata.sh # or processmc.sh, processlfv.sh
```
