#!/usr/bin/python

########################################################
#                                                      #
# reducer for creating a histogram of namespace count  #
#                                                      #
########################################################


import sys

current_namespace = None
cum_count = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    namespace,count = line.strip().split("\t")
    count = int(count) 

    # if we've encounter namespace before, add to running total
    if current_namespace == namespace:
        
        count = int(count) 
        cum_count +=count

    # if it's a new namespace
    else: 
        # if !None emit old namespace
        if current_namespace:
            print "%s\t%s" %(current_namespace, cum_count)

        # begin data colletion on new namespace
        current_namespace = namespace
        cum_count = count

print "%s\t%s" %(current_namespace, cum_count)
    

