#!/bin/bash

#SBATCH -J LFV
#SBATCH -p gpu,cpu -x gpu-0-2,gpu-0-1
#SBATCH -N 1
#SBATCH --output=/dev/null
#SBATCH --error=/dev/null
#SBATCH --open-mode=append
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1gb 
#SBATCH --comment python
#SBATCH --time 03:00:00
#SBATCH --hint=compute_bound

year=$1
infile=$2
outpath=$3
outfile=$4
workdir=$5
logdir=$6

source /opt/ohpc/pub/utils/conda/anaconda3/etc/profile.d/conda.sh
cd $workdir
conda activate py36
echo "python processonefile.py -Y $year -I $infile -O ${outpath}/${outfile} > ${logdir}/${outfile%%root}log"
python processonefile.py -Y $year -I $infile -O ${outpath}/${outfile} > ${logdir}/${outfile%%root}log
