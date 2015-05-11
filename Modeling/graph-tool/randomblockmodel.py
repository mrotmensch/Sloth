import graph_tool.all as gt
import graph_tool
import scipy
from numpy.random import poisson,randint

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

                        
gt.graph_draw(g, vertex_fill_color=bm, edge_color="black", output="blockmodel.pdf")


print(g.num_vertices(), g.num_edges())

state = gt.minimize_nested_blockmodel_dl(g, deg_corr=True)

t = gt.get_hierarchy_tree(state)

tree,label,order = t
bstack = state.get_bstack()

gt.graphviz_draw(tree,layout="sfdp",output="blockmodelhierarchytree.pdf")

'''
graph_tool.draw.draw_hierarchy(bstack[1])

gt.graphviz_draw(bstack[3])

for v in g.vertices():
    print(v.properties)
'''