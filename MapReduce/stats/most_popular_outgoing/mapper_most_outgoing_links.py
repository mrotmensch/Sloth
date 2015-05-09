#!/usr/bin/python

import sys
import string
import os


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    try:
        list_v = list(eval(line.strip()))
        id_outgoing = list_v[0]
	    id_outgoing = int(id_outgoing) # to make sure that it isn't a missing value!
        print "%d\t%d" %(id_outgoing,1)
    except:
    	pass
