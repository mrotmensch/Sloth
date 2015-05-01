#!/usr/bin/python

import sys
import string
import os


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    # get file name for positions
    file_name = os.environ['mapreduce_map_input_file']

    
    ## for links
    if "0000" in file_name: #links
        
        try:
            list_v = eval(line.strip())

            title = list_v[2]

            if title == " " or len(title) == 0:
                title = "MemptystringR"


            #vals = list(list_v[:2])
            #vals.append(list_v[3])
            from_id = str(list_v[0])

            #newww = map(str, vals)

            #new = delim.join(newww)
           
            #make sure both namespaces are 0
            if str(list_v[1])=='0' and str(list_v[3])=='0':
                print "%s\t%s|%s" %(title, "links", from_id)
        except:
            pass
            #print "%s\t%s|%s" %("error", "links", line)



    else:
        try:
    
            replaced = line.replace("NULL"," 'NULL' ")
            #try:
            list_v = list(eval(replaced))

            title = list_v.pop(2)

            if title == " " or len(title) == 0:
                title = "MemptystringR"

            #newww = map(str, list_v)

            #new = delim.join(newww)
            to_id = str(list_v[0])
            
            if str(list_v[1])=='0':
                print "%s\t%s|%s" %(title, "pages", to_id)

        except:
            pass
            #print "%s\t%s|%s" %("error", "links", line)





  


    


