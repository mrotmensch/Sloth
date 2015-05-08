import graph_tool.all as gt
import json
import os
import sys
sys.path.append('../misc')
import utils
import time

import argparse
parser = argparse.ArgumentParser(description='Select purge threshold.')
parser.add_argument('threshold', metavar='N', type=str, nargs='+',
                   help='option number')

args = parser.parse_args()
threshold_str = args.threshold[0]

threshold = float(threshold_str)
fulltree = True

loadfilename = 'graph14_pagerank_purge_%s_nested_U' % threshold_str
savefilename = 'test_json_%sU' % threshold_str

loadpath = os.path.join('/scratch/jmj418/Sloth',loadfilename)
savepath = os.path.join('../Trees',threshold_str+'U')
os.system('mkdir -p %s' % savepath)
savepath = os.path.join(savepath,savefilename)

print 'loading state'
sys.stdout.flush()
state = utils.pickleLoad(loadpath+'.pk1')

state.print_summary()
sys.stdout.flush()

def getMaxCentrality(gv,centrality_prop,label,nodeid):
    maxcentrality = -1
    maxV = None
    maxName = None
    maxNodeID = None
    for v in gv.vertices():
        mypr = centrality_prop[v]
        if mypr > maxcentrality:
            maxV = v
            maxcentrality = mypr
            maxName = label[v]
            maxNodeID = nodeid[v]
    return maxName, maxNodeID, maxV, maxcentrality


def getTreeTop(state,centrality=gt.pagerank,directed=True):
    g = state.g

    g.set_directed(directed)

    label = g.vertex_properties['label']
    nodeid = g.vertex_properties['nodeid']

    tree, inlevelblocklabels, order = gt.get_hierarchy_tree(state)

    treetop = tree
    treetop_label = treetop.new_vertex_property('string')
    for v in treetop.vertices():
        if treetop.vertex_index[v] < g.num_vertices():
            treetop_label[v] = label[v]

    treecentrality = treetop.new_vertex_property('double')
    treeroot = treetop.new_graph_property('int32_t')
    treetop.graph_properties['root'] = treeroot

    rootid = tree.num_vertices() - 1
    treetop.graph_properties['root'] = rootid

    j = g.num_vertices()
    count = 0

    s = state.project_level(0)
    blocks = set(s.get_blocks().get_array())
    propmap = s.get_blocks()
    for b in range(len(blocks)):
        assert inlevelblocklabels[tree.vertex(j)] == b, "b %s and inlevelblocklabels %s do not match up" % (b, inlevelblocklabels[tree.vertex(j)])
        gv = gt.GraphView(g, vfilt= lambda v: propmap[v] == b)
        print '%d of %d blocks' % (b, len(blocks)-1)
        try:
            centrality_prop = centrality(gv)
            for v in gv.vertices():
                treecentrality[v] = centrality_prop[v]
        except:
            pass
        j=j+1
        sys.stdout.flush()

    treetop.vertex_properties['label'] = treetop_label
    treetop.vertex_properties['centrality'] = treecentrality

    return treetop


directed = {}
directed['D'] = True
directed['U'] = False

centralities = {}
centralities['pagerank'] = gt.pagerank
centralities['betweenness'] = lambda g: gt.betweenness(g)[0]
centralities['closeness'] = gt.closeness
centralities['katz'] = gt.katz
centralities['hits'] = lambda g: gt.hits(g)[2]

exclusions = [['U','katz']]

times = []

for dname,d in directed.iteritems():
    for cname,centrality in centralities.iteritems():
        if [dname,cname] not in exclusions:
            start = time.time()

            mysavepath = "%s_%s%s" % (savepath,dname,cname)

            print '------------------%s %s------------------' % (dname,cname)
            print 'generating tree'
            print mysavepath
            sys.stdout.flush()

            treetop = getTreeTop(state,centrality=centrality,directed=d)
            treetop.save(mysavepath+'.gt',fmt='gt')
            treetop_label = treetop.vertex_properties['label']
            treecentrality = treetop.vertex_properties['centrality']

            def jsonTree(v,tree):
                d = {}
                d['id'] = tree.vertex_index[v]
                d['name'] = tree.vertex_properties['label'][v]
                d['centrality'] = treecentrality[v]
                if v.out_degree() > 0:
                    d['children'] = []
                    for u in v.out_neighbours():
                        d['children'].append(jsonTree(u,tree))
                return d

            rootid = treetop.graph_properties['root']
            json_full = jsonTree(treetop.vertex(rootid),treetop)

            def generateTendrils(dict_tree,limit=2):
                def generateTendrils_(dict_tree,tendrils={},limit=2):
                    def searchStubs(dict_tree,depth=0,limit=2):
                        myid = dict_tree['id']
                        mylabel = dict_tree['name']
                        d = {}
                        d['id'] = myid
                        d['name'] = mylabel
                        if 'children' in dict_tree.keys() and depth < limit:
                            d['children'] = []
                            for child in dict_tree['children']:
                                d['children'].append(searchStubs(child,depth=depth+1,limit=limit))
                        return d

                    myid = dict_tree['id']
                    tendrils[myid] = searchStubs(dict_tree,depth=0,limit=limit)
                    if 'children' in dict_tree.keys():
                        for child in dict_tree['children']:
                            generateTendrils_(child,tendrils,limit)
                tendrils = {}
                generateTendrils_(dict_tree,tendrils,limit)
                return tendrils

            json_tendrils = generateTendrils(json_full,limit=2)

            # spot check
            def printSpotCheck(tree):
                print ' ',tree['id'],tree['name']
                if 'children' in tree.keys():
                    for child in tree['children']:
                        print '   ',child['id'],child['name']
                        if 'children' in child.keys():
                            for grandchild in child['children']:
                                print '     ',grandchild['id'],grandchild['name']
                            
            print '\n>>>>> spot check json tendrils'
            printSpotCheck(json_tendrils[rootid])

            print '\n>>>>> spot check json full'
            printSpotCheck(json_full)

            sys.stdout.flush()

            def nameNodesBackwards(tree,n=3,maxn=None,prune=True):
                def nameNodesBackwards_(tree,n,maxn,prune):
                    maxcheck = lambda x: (maxn==None) or (x<=max(n,maxn))

                    if 'children' in tree.keys():
                        topn = []
                        totalbranches = 0
                        for child in tree['children']:
                            child_topn,branches = nameNodesBackwards_(child,n,maxn,prune)
                            topn.append(child_topn)
                            totalbranches += branches
                        if totalbranches == 1:
                            for key in tree.keys():
                                tree[key] = tree['children'][0][key]
                            return topn[0],1
                        else:
                            topn = sorted([x[-1] for x in topn],key=lambda x:x[0])
                            if maxcheck(len(topn)) == False:
                                if totalbranches == 0:
                                    topn = topn[-n:]
                                else:
                                    topn = topn[-maxn:]
                            tree['name'] = ",\n".join([x[1] for x in topn])
                            return topn,max(totalbranches,1)
                    else:
                        name = tree['name']
                        tree['name'] = "%s %0.4f" % (name,tree['centrality'])
                        return [[tree['centrality'],name]],0
                newtree = tree.copy()
                nameNodesBackwards_(newtree,n,maxn,prune)
                return newtree

            
            utils.pickleIt((json_full,json_tendrils),mysavepath+'.pk1')

            json_dump = json.dumps(json_full,sort_keys=True,indent=4, separators=(',', ': '))

            with open(mysavepath+'.json','w+') as file:
                file.write(json_dump)
                file.flush()

            diff = time.time() - start
            timestr = '%s %s   %0.3f' % (dname,cname,diff)
            print timestr
            sys.stdout.flush()
            times.append(timestr)

print '---------------- finished ---------------\n' 
for t in times:
    print t
sys.stdout.flush()