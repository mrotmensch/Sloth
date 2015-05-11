#!/bin/bash

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
