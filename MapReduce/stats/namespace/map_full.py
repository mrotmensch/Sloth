#!/usr/bin/python

########################################################
#                                                      #
# mapper for creating a histogram of namespace count   #
#                                                      #
########################################################

import sys
import string
import os


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    # split line
    s = line.split(',')
    # save only the page naamespace
    namespace = str(s[1])

    # if namespace can be turned into an integer (and is not a missing value), emit count.
    try:
	namespace = int(namespace) 
        print "%d\t%d" %(namespace, 1)
    except:
        pass




  


    


