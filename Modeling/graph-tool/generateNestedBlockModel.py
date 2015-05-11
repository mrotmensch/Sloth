import graph_tool.all as gt
import graph_tool
import scipy
from numpy.random import poisson,randint
import numpy as np
import os
import pickle
import time
import sys
import math

import argparse
parser = argparse.ArgumentParser(description='Select purge threshold.')
parser.add_argument('threshold', metavar='N', type=str, nargs='+',
                   help='option number')

args = parser.parse_args()
threshold_str = args.threshold[0]

threshold = float(threshold_str[:-1])
if threshold_str[-1] == 'U':
    directed = False
elif threshold_str[-1] == 'D':
    directed = True
else:
    raise NameError('unrecognized input %s' % threshold_str)

start = time.time()
if threshold > 0:
    filename = 'graph14_pagerank_purge_%s' % threshold_str[:-1]
else:
    filename = 'graph14_pagerank'

suffix = 'nested'
path = '/scratch/jmj418/Sloth'
loadpath = os.path.join(path,filename+'.gt')
savepath = os.path.join(path,"%s_%s.pk1" % (filename,suffix))

g = gt.load_graph(loadpath)
g.set_directed(directed)
pagerank = g.vertex_properties['pagerank']

sys.stdout.write("%d nodes, %d edges\n" % (g.num_vertices(), g.num_edges()))

sys.stdout.write("generating nested block model\n")
sys.stdout.flush()
state = gt.minimize_nested_blockmodel_dl(g, deg_corr=True)
state.print_summary()

sys.stdout.write("finished nested block model\n")
sys.stdout.flush()

def pickleIt(pyName, outputName):
    output = open(outputName, 'wb')
    pickle.dump(pyName, output)
    output.close()

print("saving")
sys.stdout.flush()
savelist = (g,state)
pickleIt(state, savepath)


diff = time.time() - start

nodes = g.num_vertices()
edges = g.num_edges()

nodesunits = ''
edgesunits = ''
if nodes >= 1000:
    nodesunits = 'k'
elif nodes >= 1000000:
    nodesunits = 'M'
if edges >= 1000:
    edgesunits = 'k'
elif edges >= 1000000:
    edgesunits = 'M'

filename = '%s_%s_%d%sN_%d%sE' % (filename,suffix,nodes/1000000,nodesunits,edges/1000000,edgesunits)
with open(filename+'.txt','w+') as f:
    f.write("%d nodes %d edges\n" % (nodes,edges))

    hours = math.floor(diff/3600.0)
    min = math.floor((diff % 3600)/60.0)
    sec = math.floor((diff % 60))

    timetocomplete = "time to complete = %0.0f hrs %0.0f min %0.0f sec\n" % (hours,min,sec)
    sys.stdout.write(timetocomplete)
    sys.stdout.flush()

    f.write(timetocomplete)
    f.write("time=%0.2f seconds\n" % diff)


