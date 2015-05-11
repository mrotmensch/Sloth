#!/usr/bin/python
#######################################################################
#                                                                     #
# reducer a program detecting top 3 articles with most outgoing links #
#                                                                     #
#######################################################################

import sys
import bisect

# since we only care about top 3, we make sure to only save those rather than the counts of the entire title list to avoid running out of memory.
# operating under the assumption that there aren't many pages with the exact same number of incoming links.


current_title = None

cum_count = 0

top_3 = [0,0,0]
top_name = [None,None,None]

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    title,count = line.strip().split("\t")

    count = int(count) 

    # if we've encounter title before, add count to running total
    if current_title == title:
        cum_count +=count

    # if it's a new namespace
    else: 

	
        if current_title:
	    index_right = bisect.bisect(top_3,cum_count)
	    index_left = bisect.bisect_left(top_3,cum_count)
	    if index_right >0 : #greater than or equal to one of top 3.
    		top_3[index_left:index_left] = [cum_count]
    		top_name[index_left:index_left] = [current_title]
    		top_3.pop(0)
    		top_name.pop(0)
	# update to new title and count
	current_title = title
	cum_count = count


for i,c in enumerate(top_3):
    print "%s\t%d" %(top_name[i],c)
