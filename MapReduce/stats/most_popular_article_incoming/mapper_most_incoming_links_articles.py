#!/usr/bin/python

import sys
import string
import os


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    try:
        list_v = list(eval(line.strip()))
        title_incoming = list_v[2]
        if str(list_v[1])=='0' and str(list_v[3])=='0':
            if title_incoming != " " and len(title_incoming)!=0:
                print "%s\t%d" %(title_incoming,1)
    except:
        pass
