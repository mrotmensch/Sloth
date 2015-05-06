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

	def __init__(self,loadpath,indent=4,separators=(',', ': ')):
		full,tendrils = utils.pickleLoad(loadpath)
		
		self.full = full
		self.tendrils = tendrils
		self.json_full = json.dumps(full,sort_keys=True, indent=indent, separators=separators)

		json_tendrils = {}
		for k,v in tendrils.iteritems():
			json_tendrils[k] = json.dumps(v,sort_keys=True, indent=indent, separators=separators)

		self.json_tendrils = json_tendrils

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





