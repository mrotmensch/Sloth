#!/usr/bin/python

import sys

current_key = None
page_val = []
links_val = []


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
 
    keys, temp = line.strip().split("\t")
    file_name, vals = temp.strip().split("|")

    #vals = vals.split("YitongWang")
 
    if current_key == keys:
        if file_name == "links":
            links_val.append(vals)
        else:
            page_val.append(vals)


    else:
        if current_key:
            if (len(links_val)>0) and (len(page_val)>0):
                for i in links_val:
                    for j in page_val:
                        #combined = i+ j # links_val+page_val. from_id + to_id
                        print "%s\t%s" %(i, j)
             
        #reset defaults
        page_val = []
        links_val = []

        #process new information
        current_key = keys
        if file_name == "links":
            links_val.append(vals)
        else:
            page_val.append(vals)


if (len(links_val)>0) and (len(page_val)>0):
    for i in links_val:
        for j in page_val:
            #combined = i+ j # trips_val+fares_val
            #print "%s\t%s" %(current_key, combined)
            print "%s\t%s" %(i, j)


