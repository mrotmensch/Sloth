#!/usr/bin/python

##############################################################################################
#  mapper_full.py                                                                            #
#  This program deals with the merging of the parsed Pagelinks and Pages files.              #
#                                                                                            #
##############################################################################################



import sys
import string
import os


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    # get file name for positions
    file_name = os.environ['mapreduce_map_input_file']

    
    ## for pagelinks
    if "0000" in file_name: #links
        
        try:
            list_v = eval(line.strip())

            # get article title
            title = list_v[2]

            # replace empty string title into a unique replacement
            # remember that we are getting ride of titles in the reducer, so we only care it's unique and matches.
            if title == " " or len(title) == 0:
                title = "MemptystringR"

            # get source_id
            from_id = str(list_v[0])

           
            #make sure both namespaces are 0
            if str(list_v[1])=='0' and str(list_v[3])=='0':
                print "%s\t%s|%s" %(title, "links", from_id)
        except:
            pass
            
    # for pages
    else:
        try:
            # replace Null with string "Null" so it can be evaluated properly
            replaced = line.replace("NULL"," 'NULL' ")
        
            list_v = list(eval(replaced))

            # get article title
            title = list_v.pop(2)

            # replace empty string title into a unique replacement
            # remember that we are getting ride of titles in the reducer, so we only care it's unique and matches.
            if title == " " or len(title) == 0:
                title = "MemptystringR"

            
            to_id = str(list_v[0])
            
            if str(list_v[1])=='0':
                print "%s\t%s|%s" %(title, "pages", to_id)

        except:
            pass
            





  


    


