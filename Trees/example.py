import graphTree
import os

loadpath = '1e-5/json_1e-5_Dbetweenness.pk1'

savepath_jsonfull = 'example_output.json'
savepath_jsontendrils = 'example_tendrils'

os.system('mkdir -p %s' % savepath_jsontendrils)

tree = graphTree.graphTree(loadpath)

tendrils,json_tendrils = tree.regenerateTendrils(limit=2)

tree.tofile_full(savepath_jsonfull)
tree.tofile_tendrils(savepath_jsontendrils)
