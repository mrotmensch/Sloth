import graph_tool.all as gt
import json
import os
import sys
sys.path.append('../misc')

import utils

def nameNodesBackwards(tree,n=3,maxn=None,prune=True):
    maxcheck = lambda x: (maxn==None) or (x<=max(n,maxn))

    if 'children' in tree.keys():
        topn = []
        totalbranches = 0
        for child in tree['children']:
            child_topn,branches = nameNodesBackwards(child,n,maxn,prune)
            topn.append(child_topn)
            totalbranches += branches
        if totalbranches == 1:
            for key in tree.keys():
                tree[key] = tree['children'][key]
            return topn[0],1
        else:
            topn = sorted([x[-1] for x in topn],key=lambda x:x[0])
            if maxcheck(len(topn)) == False:
                topn = topn[-maxn:]
            tree['name'] = ",\n".join([x[1] for x in topn])
            return topn,max(totalbranches,1)
    else:
        return [tree['centrality'],tree['name']],0


tree,tendrils = utils.pickleLoad('../Trees/5e-5/json_5e-5_Dbetweenness.pk1')

newtree = nameNodesBackwards(tree)






