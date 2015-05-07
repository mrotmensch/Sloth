import graph_tool.all as gt
import graph_tool
import time
import math
import os

start = time.time()

filename = 'graph14'
path = '/scratch/jmj418/Sloth'
loadpath = os.path.join(path,filename+'.gt')
savepath = os.path.join(path,filename+'_Upagerank.gt')

g = gt.load_graph(loadpath)

print(g.num_vertices(), g.num_edges())

g.set_directed(False)

pagerank = graph_tool.centrality.pagerank(g)

g.vertex_properties['pagerank'] = pagerank

g.save(savepath)

diff = time.time() - start

nodes = g.num_vertices()
edges = g.num_edges()

filename = 'pagerank_%s_%dMN_%dME' % (filename,nodes/1000000,edges/1000000)
with open(filename+'.txt','w+') as f:
    f.write("test: %d nodes %d edges\n" % (nodes,edges))

    hours = math.floor(diff/3600.0)
    min = math.floor((diff % 3600)/60.0)
    sec = math.floor((diff % 60))
    
    timetocomplete = "time to complete = %0.0f hrs %0.0f min %0.0f sec\n" % (hours,min,sec)
    print timetocomplete

    f.write(timetocomplete)
    f.write("time=%0.2f seconds\n" % diff)
