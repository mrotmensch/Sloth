import graph_tool.all as gt
import numpy as np
import sys
import os

import argparse
parser = argparse.ArgumentParser(description='Select purge threshold.')
parser.add_argument('threshold', metavar='N', type=str, nargs='+',
                   help='option number')

args = parser.parse_args()
threshold_str = args.threshold[0]

threshold = float(threshold_str)

loadfilename = 'graph_pagerank'
savefilename = loadfilename+'_purge_'+threshold_str

print 'loadfile = %s' % loadfilename
print 'savefile = %s' % savefilename

path = '../graphs'
loadpath = os.path.join(path,loadfilename+'.gt')
savepath = os.path.join(path,savefilename+'.gt')

print 'loadpath = %s' % loadpath
print 'savepath = %s' % savepath
sys.stdout.flush()

print '>> loading graph'
sys.stdout.flush()
g = gt.load_graph(loadpath)

pagerank = g.vertex_properties['pagerank']

print '>> graph loaded'
print '%d nodes, %d edges' % (g.num_vertices(),g.num_edges())
sys.stdout.flush()

print '>> filtering graph'
sys.stdout.flush()
g = gt.GraphView(g, vfilt=lambda v: pagerank[v] > threshold)

print '>> graph filtered'
print '%d nodes, %d edges' % (g.num_vertices(),g.num_edges())
sys.stdout.flush()

print '>> purging'
sys.stdout.flush()
g.purge_vertices()

print '>> purged'
print '%d nodes, %d edges' % (g.num_vertices(),g.num_edges())
sys.stdout.flush()

print '>> saving'
sys.stdout.flush()

g.save(savepath,fmt='gt')

print '>> finished'
sys.stdout.flush()
