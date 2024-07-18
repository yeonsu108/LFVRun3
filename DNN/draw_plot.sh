folder=DNN_out_0705
postfix=_orgbin

cd $folder

cd 2018_postprocess
../../../plotIt/plotIt -o ../figure_2018/ ../../../plotIt/configs/TOP-22-011/config_2018.yml -y -s --allSig
../../../plotIt/plotIt -o ../figure_2018/ ../../../plotIt/configs/TOP-22-011/config_2018.yml
cd ../2017_postprocess
../../../plotIt/plotIt -o ../figure_2017/ ../../../plotIt/configs/TOP-22-011/config_2017.yml -y -s --allSig
../../../plotIt/plotIt -o ../figure_2017/ ../../../plotIt/configs/TOP-22-011/config_2017.yml
cd ../2016post_postprocess
../../../plotIt/plotIt -o ../figure_2016post/ ../../../plotIt/configs/TOP-22-011/config_2016post.yml -y -s --allSig
../../../plotIt/plotIt -o ../figure_2016post/ ../../../plotIt/configs/TOP-22-011/config_2016post.yml
cd ../2016pre_postprocess
../../../plotIt/plotIt -o ../figure_2016pre/ ../../../plotIt/configs/TOP-22-011/config_2016pre.yml -y -s --allSig
../../../plotIt/plotIt -o ../figure_2016pre/ ../../../plotIt/configs/TOP-22-011/config_2016pre.yml

cd ../../

python ../nanoaodframe/print_syst_table.py -I $folder --postfix _orgbin -D -Y 2016pre
python ../nanoaodframe/print_syst_table.py -I $folder --postfix _orgbin -D -Y 2016post
python ../nanoaodframe/print_syst_table.py -I $folder --postfix _orgbin -D -Y 2017
python ../nanoaodframe/print_syst_table.py -I $folder --postfix _orgbin -D -Y 2018

cd $folder

cd 2018_postprocess$postfix
../../../plotIt/plotIt -o ../figure_2018$postfix/ ../../../plotIt/configs/TOP-22-011/config_2018.yml -y -s --allSig
../../../plotIt/plotIt -o ../figure_2018$postfix/ ../../../plotIt/configs/TOP-22-011/config_2018.yml
cd ../2017_postprocess$postfix
../../../plotIt/plotIt -o ../figure_2017$postfix/ ../../../plotIt/configs/TOP-22-011/config_2017.yml -y -s --allSig
../../../plotIt/plotIt -o ../figure_2017$postfix/ ../../../plotIt/configs/TOP-22-011/config_2017.yml
cd ../2016post_postprocess$postfix
../../../plotIt/plotIt -o ../figure_2016post$postfix/ ../../../plotIt/configs/TOP-22-011/config_2016post.yml -y -s --allSig
../../../plotIt/plotIt -o ../figure_2016post$postfix/ ../../../plotIt/configs/TOP-22-011/config_2016post.yml
cd ../2016pre_postprocess$postfix
../../../plotIt/plotIt -o ../figure_2016pre$postfix/ ../../../plotIt/configs/TOP-22-011/config_2016pre.yml -y -s --allSig
../../../plotIt/plotIt -o ../figure_2016pre$postfix/ ../../../plotIt/configs/TOP-22-011/config_2016pre.yml
cd ../../

python ../nanoaodframe/stack_signals_v2.py -I $folder
python ../nanoaodframe/plot_run2.py -I $folder -D -y
python ../nanoaodframe/plot_run2.py -I $folder -D

python ../nanoaodframe/stack_signals_v2.py -I $folder --postfix _orgbin
python ../nanoaodframe/plot_run2.py -I $folder --postfix _orgbin -D -y
python ../nanoaodframe/plot_run2.py -I $folder --postfix _orgbin -D

