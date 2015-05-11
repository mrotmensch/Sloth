#!/usr/bin/python

##############################################################################################
#  reducer.py                                                                                #
#                                                                                            #
#  This serves as the reducer for both mapper_pagelinks.py and mapper_pages.py.              #
#  This is an identity reducer                                                               #
##############################################################################################

import sys


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    key,something = line.strip().split("\t")
    print "%s\t%s" %(key, "")

