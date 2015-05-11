import sys
sys.path.append('../misc')

import os
import utils
import json

class graphTree():

	'''
	full            nested dictionaries of full tree
	tendrils        tendrils[k] = nested dictionary of node k and its children
	json_full       full tree in json format (string)
	json_tendrils   json_tendrils[k] = tendrils[k] in json format (string)
	'''

	full = None
	tendrils = None
	json_full = None
	json_tendrils = None

	_indent = None
	_separators = None

	def __init__(self,loadpath,indent=4,separators=(',', ': ')):
		full,tendrils = utils.pickleLoad(loadpath)
		
		self.full = full
		self.tendrils = tendrils
		self.json_full = json.dumps(full,sort_keys=True, indent=indent, separators=separators)

		json_tendrils = {}
		for k,v in tendrils.iteritems():
			json_tendrils[k] = json.dumps(v,sort_keys=True, indent=indent, separators=separators)

		self.json_tendrils = json_tendrils
		self._indent = indent
		self._separators = separators

	def tofile_full(self,savepath):
		'''
		save json_tree to file
		'''
		assert self.json_full != None, "json_full is empty"
		with open(savepath,'w+') as f:
			f.write(self.json_full)
			f.flush()

	def tofile_tendrils(self,savepath):
		'''
		Will save out all tendrils as separate files.  
		Thus, savepath must be a directory.  The root of
		the tree is saved as 'root.json'.  All other files
		are saved as <key>.json
		'''
		assert os.path.isdir(savepath), "not a directory: %s" % savepath
		assert self.json_tendrils != None, "json_tendrils is empty"

		rootkey = self.full['id']
		for k,v in self.json_tendrils.iteritems():
			if k == rootkey:
				filepath = os.path.join(savepath,"root.json")
			else:
				filepath = os.path.join(savepath,"%d.json" % k)
			with open(filepath,'w+') as f:
				f.write(v)
				f.flush()

	def regenerateTendrils(self,limit=2):
		'''
		limit = max depth of tendrils
		returns tendrils, json_tendrils
		saves tendrils to self
		'''

		def regenerateTendrils_(dict_tree,tendrils={},limit=2):
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
					regenerateTendrils_(child,tendrils,limit)
		tendrils = {}
		regenerateTendrils_(self.full,tendrils,limit)
		self.tendrils = tendrils
		json_tendrils = {}
		for k,v in tendrils.iteritems():
			json_tendrils[k] = json.dumps(v,sort_keys=True, indent=self._indent, separators=self._separators)
		self.json_tendrils = json_tendrils
		return tendrils, json_tendrils



