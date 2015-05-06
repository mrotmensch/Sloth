import graphTree
import os

loadpath = 'json_1e-5_prAll.pk1'

savepath_jsonfull = 'output.json'
savepath_jsontendrils = 'tendrils'

os.system('mkdir -p %s' % savepath_jsontendrils)

tree = graphTree.graphTree(loadpath)

tree.tofile_full(savepath_jsonfull)
tree.tofile_tendrils(savepath_jsontendrils)
