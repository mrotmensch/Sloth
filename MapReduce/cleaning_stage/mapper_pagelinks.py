#!/usr/bin/python

##############################################################################################
#  mapper_pagelinks.py                                                                       #
#                                                                                            #
#  The purpose of this funciton is to parse the file enwiki-20150304-pagelinks.sql           #
#  from its sql form to a format that is readable my MapReduce                               #
#                                                                                            #
#    General comments:                                                                       #
#      1) Content lines average 1038000 charecters per line.                                 #
#      2) the longest sql comment is less than 90 charecters.                                #
#      3) sql tuples are of the following form:                                              #
#      4) sometimes the csv parser parses that need not be parse.                            #
#         so we need to check for such occurences and "re-merge" wrongly parsed portions.    #
#      5) the whole mapper exists in a try except block because a single line of the file    #
#         containing complex algebra notation cannot be parsed and raises and error.         #
#         See report for error analysis                                                      #
##############################################################################################

import sys
import string
import os
import re
import csv
import cStringIO

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    clean = line.strip()

    #remove short lines that are sql metadata. All data lines are over tens of thousand of charecters long.
    try:
        if len(clean) >300: 

            # We know that each tuple in sql starts and ends with paretheses. remove all irrelevant entries before this token.
	    # find first occurence of '(' in line
            start_index = clean.find('(')
	    # find last occurance of ')' in line
            end_index = clean.rfind(')')

            # retrieve relevant substring
            substring = clean[start_index:end_index+1]
          
            # read in substring and parse using csv parser
            new_line = cStringIO.StringIO(substring)
            temp = csv.reader(new_line, delimiter=',')

            parsed_line = temp.next() #only one line in a generator.

	    # prepare delimitaer for re-merging
            delim = ','
            delim2 = ''
            step=4
            start_counter = 0
            end_counter = step
            extra = 0
            
	    # cycle through parsed elements in a line.
            while end_counter < len(parsed_line):
                
                # if parsed format doesn't match expected format
                if parsed_line[end_counter-1][-1] ==')':

                    #get rid of extra commas that caused extra parsing and re-merge
                    partial=[delim.join(parsed_line[start_counter:start_counter+2]),delim2.join(parsed_line[start_counter+2:end_counter-1]),parsed_line[end_counter-1]]
                    sequence = delim.join(partial)

                    # emit string merged on commas and increment counter
                    print "%s\t%s" %(sequence[1:-1], "1")
                    start_counter = end_counter
                    end_counter +=step
                else:
                    # in this format did not match, expand to next elemnt and check if it's the end element.
                    end_counter+=1

            
            #print any leftovers
            partial=[delim.join(parsed_line[start_counter:start_counter+2]),delim2.join(parsed_line[start_counter+2:-1]),parsed_line[-1]]
            sequence = delim.join(partial)
            print "%s\t%s" %(sequence[1:-1], "1")
            

    except:
        pass
       
