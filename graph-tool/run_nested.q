#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=40:00:00
#PBS -l mem=92GB
#PBS -N nested_U_5e-7
#PBS -M justinmaojones@nyu.edu
#PBS -j oe

# load necessary modules

module purge
module load python/intel/2.7.6
module load graph-tool/gnu/2.2.42

# location of the source code must be defined explicitly
SOURCEDIR=$HOME/Sloth/graph-tool
cd $SOURCEDIR

python generateNestedBlockModel_D.py '5e-7'
