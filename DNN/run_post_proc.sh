folder=DNN_out_0424
python ../nanoaodframe/postprocess.py -Y 2016pre -I $folder
python ../nanoaodframe/postprocess.py -Y 2016post -I $folder
python ../nanoaodframe/postprocess.py -Y 2017 -I $folder
python ../nanoaodframe/postprocess.py -Y 2018 -I $folder

python ../nanoaodframe/postprocess.py -Y 2016pre -I $folder --postfix _orgbin
python ../nanoaodframe/postprocess.py -Y 2016post -I $folder --postfix _orgbin
python ../nanoaodframe/postprocess.py -Y 2017 -I $folder --postfix _orgbin
python ../nanoaodframe/postprocess.py -Y 2018 -I $folder --postfix _orgbin

python ../nanoaodframe/stack_signals_v2.py -I $folder
python ../nanoaodframe/stack_signals_v2.py -I $folder --postfix _orgbin

python postprocess_2.py -I DNN_out_0424
