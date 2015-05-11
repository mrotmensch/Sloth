#!/usr/bin/python


import sys
import string
import os

################################################################################
#   mapy_full.py                                                               #
# This is the mapper for the program that creates the clean decoder between    #
# page_id's and page_title.                                                    #
#                                                                              #
################################################################################

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    try:
        # replace Null by string 'Null' so that eval can evaluate it correctly/
        replaced = line.replace("NULL"," 'NULL' ")

        # create a list of the evaluated items in the line
        list_v = list(eval(replaced))

        # extract title from tuple
        title = list_v.pop(2)

        # the reducer cannot split a key,value pair when key is " ", therefore replace it with explanatory string.
        if title == " " or len(title) == 0:
                title = "Title_is_empty_string"

        # extract id corresponding to title
        ID = str(list_v[0])
        
        # only emit if in page in article namespace
        if str(list_v[1])=='0':
            print "%s\t%s" %(ID, title)
    except:
        pass





  


    


