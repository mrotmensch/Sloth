import graph_tool.all as gt
import sys
sys.path.append('../misc')

import utils
import json
import os


loadfilename = 'graph14_pagerank_nested_1e-5_4n'
savefilename = 'json_1e-5_prAll'
path = '/scratch/jmj418/Sloth'
loadpath = os.path.join(path,loadfilename)
savepath = os.path.join(path,savefilename)

print 'loading state'
sys.stdout.flush()
state = pickleLoad(loadpath+'.pk1')

print 'drawing hierarchy'
sys.stdout.flush()
gt.draw_hierarchy(state, output=savepath+'.pdf')