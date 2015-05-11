#!/usr/bin/python

################################################################################
#                                                                              #
# This is the reducer for the program that creates the clean decoder between   #
# page_id's and page_title.                                                    #
# Output for the program is tuples of the form (Page_id, Page_title)           #                            
#                                                                              #
################################################################################

import sys


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    ID,title = line.strip().split("\t")
    print "%s\t%s" %(ID, title)

