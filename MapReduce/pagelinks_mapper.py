#!/usr/bin/python

import sys
import string
import os
import re
import csv
#import StringIO
import cStringIO

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    clean = line.strip()
    #print "%s\t%s" %(clean,None)

    
    #remove short lines that are sql metadata.
    if len(clean) >200: 

        #remove everything before first ''. useful for first input line.
        start_index = clean.find('(')
        end_index = clean.rfind(')')

        
        substring = clean[start_index:end_index+1]
      
        
        new_line = cStringIO.StringIO(substring)
        temp = csv.reader(new_line, delimiter=',')

        parsed_line = temp.next() #only one line in a generator.
        delim = ','
        delim2 = ''

        step=4
        start_counter = 0
        end_counter = step
        extra = 0
        
        while end_counter < len(parsed_line):
            
    
            if parsed_line[end_counter-1][-1] ==')':

                #get rid of extra commas and merge
                partial=[delim.join(parsed_line[start_counter:start_counter+2]),delim2.join(parsed_line[start_counter+2:end_counter-1]),parsed_line[end_counter-1]]

                sequence = delim.join(partial)


                print "%s\t%s" %(sequence[1:-1], "1")
                start_counter = end_counter
                end_counter +=step
            else:
                end_counter+=1

        
        #print any leftovers
        partial=[delim.join(parsed_line[start_counter:start_counter+2]),delim2.join(parsed_line[start_counter+2:-1]),parsed_line[-1]]

        sequence = delim.join(partial)
        print "%s\t%s" %(sequence[1:-1], "1")
        

    
   