#!/bin/bash

#SBATCH -J LFV
#SBATCH -p gpu,cpu -x gpu-0-2,compute-0-1,gpu-0-1,compute-0-3
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
intree=$5
outtree=$6
workdir=$7
logdir=$8
datasetname=$9

source /opt/ohpc/pub/utils/conda/anaconda3/etc/profile.d/conda.sh
cd $workdir
conda activate py36
echo "python skimonefile.py -Y $year $infile ${outpath}/${outfile} $intree $outtree > ${logdir}/${outfile%%root}log"
python skimonefile.py -Y $year $infile ${outpath}/${outfile} $intree $outtree > ${logdir}/${outfile%%root}log
