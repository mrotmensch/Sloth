#!/bin/bash
#PBS -l nodes=2:ppn=20
#PBS -l walltime=35:00:00
#PBS -l mem=40GB
#PBS -N loadgraph9-test
#PBS -M justinmaojones@nyu.edu
#PBS -j oe

# load necessary modules

module purge
module load intel/14.0.2
module load scipy/intel/0.15.1
module load expat/intel/2.1.0
module load sparsehash/intel/2.0.2
module load cairomm/intel/1.11.2
module load cgal/intel/4.5
module switch boost/intel/1.55.0 boost/gnu/1.55.0
module load python/intel/2.7.6
module load graph-tool/gnu/2.2.42

# define location of working directory when the HPC gets going

# run source code
# location of the source code must be defined explicitly
SOURCEDIR=$HOME/Sloth/graph-tool
cd $SOURCEDIR
python loadgraph.py
