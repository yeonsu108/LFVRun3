## DNN with 3 features - Train, Evaluation, Draw Histograms
### 0. Presets
```{.Bash}
conda activate py36
source source /opt/ohpc/pub/root/root_v6.26.06_gcc540/bin/thisroot.sh
```
ROOT_6.26.06 with python 3.6 is installed in htop.
 
### 1. Train
```{.Bash}
python train.py
```
**Train** is performed using processed ntuples in `../nanoaodframe_*LFV/` and corresponding part should be **MODIFIED**.

Training is performed with signal (LFV sample mixture) and background (tt semileptonic and dileptonic mixture) samples.

When training is done, `./<train output folder>/` will be generated (e.g. TTnov_01_norm_20nodes_3layers_s1b1) with result plots (correlation, loss, accuracy, DNN output, confusion matrix).

Best model is stored in the output folder as `best_model.h5`.

### 2. Evaluation, post processing, drawing
```{.Bash}
python eval.py
python postprocess.py
python stack_signals.py
python plot_run2.py
```
**Evaluation** is performed with the best model from training and produce dnn output score histograms with data and MC samples.

To use proper model, you must check the directory of the processed ntuple used in training.

The output folder is defined in `eval.py`. The folders will appear by year (run). **Currently, you need to put your model in 'nom' folder**

The post processing is to gather all uncertainty histograms into a single, nominal root file, and apply b tagging rescaling.

The plotIt does not support stack for signals, thus it is done by dedicated code.

The `plot_run2.py` will read information from existing configs for each year, then combine into one, usint templates.


### Advanced
> To modify some details of the plots from training, cross section for normalization, histogram styles, modules in `utils/` folder will be helpful.
