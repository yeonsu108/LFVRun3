## DNN with 3 features - Train, Evaluation, Draw Histograms
### 0. Presets
```{.Bash}
#check if modules are properly loaded
ml list
> Currently Loaded Modules:
>   1) ohpc   2) gnu8/8.3.0   3) boost/1.63.0_gcc830   4) cuda/11.8

conda activate py36
source /opt/ohpc/pub/root/root_v6.26.06_gcc830/bin/thisroot.sh
```
ROOT_6.26.06 with python 3.6 is installed in htop.
 
### 1. Train
#### 1.1. Train 2 separate binary class classification 
```{.Bash}
python train.py
```
**Train** is performed using processed ntuples in `../nanoaodframe_*LFV/` and corresponding part should be **MODIFIED**.

Training is performed with signal (LFV sample mixture) and background (tt semileptonic and dileptonic mixture) samples.

When training is done, `./<train output folder>/` will be generated (e.g. TTnov_01_norm_20nodes_3layers_s1b1) with result plots (correlation, loss, accuracy, DNN output, confusion matrix).

Best model is stored in the output folder as `best_model.h5`.
#### 1.2. Train 2 separate multi class classification 
```{.Bash}
python train_multi.py
```


### 2. Evaluation, post processing, drawing
#### 2.1. Binary class
```{.Bash}
python eval.py
```
In order to run the following scripts you need provide an option.
For now allowed options are:
'rerun_multi_Multiaug22','rerun_staug22', 'rerun_ttaug22'
If you run with out changing the label it will run the st channel.
If you have not compile the plotlt yet please follow the read me in the plotlt.
```{.Bash}
python postprocess.py -L rerun_staug22
python stack_signals.py -L rerun_staug22
python plot_run2.py -L rerun_staug22
```
**Evaluation** is performed with the best model from training and produce dnn output score histograms with data and MC samples.

To use proper model, you must check the directory of the processed ntuple used in training.

The output folder is defined in `eval.py`. The folders will appear by year (run). **Currently, you need to put your model in 'nom' folder**

The post processing is to gather all uncertainty histograms into a single, nominal root file, and apply b tagging rescaling.

The plotIt does not support stack for signals, thus it is done by dedicated code.

The `plot_run2.py` will read information from existing configs for each year, then combine into one, usint templates.
#### 2.2. multi class

```{.Bash}
python haddToMergeBkg.py
python eval.py
python postprocess.py -L rerun_multi_Multiaug22
python haddToMergeSig.py
python stack_signals.py -L rerun_multi_Multiaug22
python plot_run2.py -L rerun_multi_Multiaug22
```

### Advanced
> To modify some details of the plots from training, cross section for normalization, histogram styles, modules in `utils/` folder will be helpful.
