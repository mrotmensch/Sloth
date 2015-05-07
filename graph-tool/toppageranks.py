import graph_tool.all as gt
import numpy as np

g1 = gt.load_graph('/scratch/jmj418/Sloth/graph14_pagerank.gt')

g2 = gt.load_graph('/scratch/jmj418/Sloth/graph14_Upagerank.gt')


def listMaxPageRanks(g,top=20):
	pagerank = g.vertex_properties['pagerank']
	x = np.sort(np.array(pagerank.get_array()))
	threshold = x[-top]
	gg = gt.GraphView(g,vfilt = lambda v: pagerank[v] >= threshold)
	nodes = []

	pagerank = gg.vertex_properties['pagerank']
	label = gg.vertex_properties['label']
	for v in gg.vertices():
		nodes.append([pagerank[v],label[v]])
	nodes = sorted(nodes,key=lambda v:v[0],reverse=True)
	print nodes


listMaxPageRanks(g1)