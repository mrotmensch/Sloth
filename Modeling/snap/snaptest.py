import snap
import time
import math
import os


nodes = 100000
edges = 1000000
print nodes,"nodes,",edges,"edges"

filename = 'snaptest_%dkN_%dkE' % (nodes/1000,edges/1000)

with open(filename+'.txt','w+') as f:
    f.write("test: %d nodes %d edges\n" % (nodes,edges))
    start = time.time()
    UGraph = snap.GenRndGnm(snap.PUNGraph, nodes, edges)
    CmtyV = snap.TCnComV()
    modularity = snap.CommunityGirvanNewman(UGraph, CmtyV)
    f.write("The modularity of the network is %f\n" % modularity)

    end = time.time()
    diff = end-start

    hours = math.floor(diff/3600.0)
    min = math.floor((diff % 3600)/60.0)
    sec = math.floor((diff % 60))

    f.write("time to complete = %0.0f hrs %0.0f min %0.0f sec\n" % (hours,min,sec))
    f.write("time=%0.2f\n" % diff)

os.system('cat %s' % (filename+'.txt'))
CmtyV.Save(snap.TFOut(filename + '.CmtyV'))

