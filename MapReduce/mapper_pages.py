#!/usr/bin/python

import sys
import string
import os
import re

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
	p = re.compile(r"\(((?:'[^\\']*'|[^()])*)\)")
	clean = line.strip()

	if len(clean) >200: #otherwise it's sql metadata.
		matches =p.findall(clean)
		for m in matches:
			#divided = m.split(",")
			print "%s\t%s" %(m,None)

	
	
	
       

