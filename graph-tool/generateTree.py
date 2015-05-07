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

loadfilename = 'graph14_pagerank_purge_%s_nested' % threshold_str
savefilename = 'json_%s' % threshold_str

loadpath = os.path.join('/scratch/jmj418/Sloth',loadfilename)
savepath = os.path.join('../Trees',threshold_str)
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
    return maxName, maxNodeID, maxV


def getTreeTop(state,centrality=gt.pagerank,directed=True,fulltree=False):
    g = state.g
    visited = []

    g.set_directed(directed)
    
    #pagerank = g.vertex_properties['pagerank']

    #g = gt.GraphView(g,vfilt=lambda v: pagerank[v] > threshold)
    label = g.vertex_properties['label']
    nodeid = g.vertex_properties['nodeid']

    tree, inlevelblocklabels, order = gt.get_hierarchy_tree(state)

    if fulltree:
        treetop = tree
        treetop_label = treetop.new_vertex_property('string')
        for v in treetop.vertices():
            if treetop.vertex_index[v] < g.num_vertices():
                treetop_label[v] = label[v]
    else:
        treetop = gt.GraphView(tree,vfilt=lambda v: tree.vertex_index[v] >= g.num_vertices())
        treetop_label = treetop.new_vertex_property('string')

    dangling = treetop.new_vertex_property('bool')
    
    numlevels = len(state.levels)
    rootid = tree.num_vertices() - 1
    j = rootid
    count = 0
    for i in range(numlevels-1,-1,-1):
        s = state.project_level(i)
        blocks = set(s.get_blocks().get_array())
        propmap = s.get_blocks()
        for b in range(len(blocks)-1,-1,-1):
            assert inlevelblocklabels[tree.vertex(j)] == b, "b %s and inlevelblocklabels %s do not match up" % (b, inlevelblocklabels[tree.vertex(j)])
            gv = gt.GraphView(g, vfilt= lambda v: (propmap[v] == b) and (label[v] not in visited))
            if gv.num_vertices() > 0:
                try:
                    centrality_prop = centrality(gv)
                    name, mynodeid, v = getMaxCentrality(gv,centrality_prop,label,nodeid)
                    visited.append(name)
                    treetop_label[treetop.vertex(j)] = name
                    dangling[treetop.vertex(j)] = False
                    print i,b,gv.num_vertices(),name,mynodeid
                except:
                    pass
            else:
                dangling[treetop.vertex(j)] = True
                print i,b,'DANGLING'
                count = count + 1
            j=j-1
            sys.stdout.flush()
    treetop.vertex_properties['label'] = treetop_label
    treetop.vertex_properties['dangling'] = dangling
    print count,"dangling vertices\n"
    return treetop,rootid


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

            print '------------------%s %s------------------' % (dname,cname)
            print 'generating tree'
            sys.stdout.flush()

            treetop,rootid = getTreeTop(state,centrality=centrality,directed=d,fulltree=fulltree)
            dangling = treetop.vertex_properties['dangling']
            treetop = gt.GraphView(treetop,vfilt=lambda v: dangling[v] == False)
            treetop_label = treetop.vertex_properties['label']
                
            # check the labels of the vertices
            for u in treetop.vertices():
                #print treetop_label[u]
                if len(treetop_label[u]) == 0:
                    print "ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            print treetop.num_vertices(), "nodes total\n"
            sys.stdout.flush()

            def jsonTree(v,tree):
                d = {}
                d['id'] = tree.vertex_index[v]
                d['name'] = tree.vertex_properties['label'][v]
                if v.out_degree() > 0:
                    d['children'] = []
                    for u in v.out_neighbours():
                        d['children'].append(jsonTree(u,tree))
                return d

            root = treetop.vertex(rootid)
            json_full = jsonTree(root,treetop)

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


            mysavepath = "%s_%s%s" % (savepath,dname,cname)
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