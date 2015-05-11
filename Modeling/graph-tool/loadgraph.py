import graph_tool.all as gt
import graph_tool

import numpy as np
import time
import sys

g = gt.Graph(directed=True)

start = time.time()

GRAPHNAME = 'graph14_int32_pass'

vertex_map={}

label_map=g.new_vertex_property('string')
nodeid_map=g.new_vertex_property('int32_t')

nodefilename = "/scratch/jmj418/Sloth/nodes.txt"
edgefilename = "/scratch/jmj418/Sloth/edges.txt"

missing_nodes = set()

sys.stdout.write("loading nodes\n")
sys.stdout.flush()
with open(nodefilename,'r') as f:
	for line in f:
		nodeid,nodename = line.replace('\n','').split('\t')
		nodeid = int(nodeid)
		vertex_map[nodeid] = g.add_vertex()
		label_map[vertex_map[nodeid]] = nodename
		nodeid_map[vertex_map[nodeid]] = nodeid


sys.stdout.write("loading edges\n")
sys.stdout.flush()
i=0
with open(edgefilename,'r') as f:
    for line in f:
	try:
            nodeid_from,nodeid_to = line.replace('\n','').split('\t')
	    nodeid_from = int(nodeid_from)
	    nodeid_to = int(nodeid_to)
	    node_from = vertex_map[nodeid_from]
	    node_to = vertex_map[nodeid_to]
	    g.add_edge(node_from,node_to)
	except:
            pass
#	    if nodeid_from not in vertex_map.keys():
#	        missing_nodes.add(nodeid_from)
#	    if nodeid_to not in vertex_map.keys():
#	        missing_nodes.add(nodeid_to)
        i = i+1
        #if i>1e6:
        #    break
        if i % 1e6 == 0:
            diff = time.time() - start
            ETA = diff/i*359000000.0/3600.0
            sys.stdout.write("%d %0.2f %0.2f hrs\n" % (i,diff,ETA))
            sys.stdout.flush()

sys.stdout.write('add property maps\n')
sys.stdout.flush()
g.vertex_properties['label'] = label_map
g.vertex_properties['nodeid'] = nodeid_map


savepath = "/scratch/jmj418/Sloth/%s.gt" % GRAPHNAME
g.save(savepath,fmt='gt')

with open("/scratch/jmj418/Sloth/%s_missingedges.txt" % GRAPHNAME,'w+') as f:
    for nodeid in missing_nodes:
        f.write("%d\n" % nodeid)

sys.stdout.write("FINISHED!\n")
sys.stdout.flush()
