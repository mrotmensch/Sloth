import graph_tool.all as gt
import graph_tool
import scipy
from numpy.random import poisson,randint
import time
import math

start = time.time()
def corr(a,b):                                                                                                                                         
    if a==b:
        return 0.999
    else:
        return 0.001
        
g, bm = gt.random_graph(100, 
                        lambda: poisson(10), 
                        directed=False,
                        block_membership=lambda: randint(50),
                        vertex_corr=corr)
                        
                        
print(g.num_vertices(), g.num_edges())
state = gt.minimize_nested_blockmodel_dl(g, deg_corr=True)


diff = time.time() - start

nodes = g.num_vertices()
edges = g.num_edges()

filename = 'undirected_%dkN_%dkE' % (nodes/1000,edges/1000)
with open(filename+'.txt','w+') as f:
    f.write("test: %d nodes %d edges\n" % (nodes,edges))

    hours = math.floor(diff/3600.0)
    min = math.floor((diff % 3600)/60.0)
    sec = math.floor((diff % 60))
    
    timetocomplete = "time to complete = %0.0f hrs %0.0f min %0.0f sec\n" % (hours,min,sec)
    print timetocomplete

    f.write(timetocomplete)
    f.write("time=%0.2f seconds\n" % diff)
