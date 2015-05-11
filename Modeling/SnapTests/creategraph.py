import snap
import pandas as pd
import os

nodes = 1000
edges = 10000
print nodes,"nodes,",edges,"edges"

filename = 'ugraph_%dkN_%dkE' % (nodes/1000,edges/1000)

UGraph = snap.GenRndGnm(snap.PUNGraph, nodes, edges)

os.system('rm -f %s.txt' % filename)
snap.SaveEdgeList(UGraph,filename+'.txt','undirected graph')

x = pd.read_csv(filename+'.txt',sep='\t',skiprows=3)

x = x+1

os.system('rm -f %s.csv' % filename)
x.to_csv(filename+'.csv',sep=',',header=False,index=False)


