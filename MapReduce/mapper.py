#!/usr/bin/python

import sys
import string
import os
import re

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    p = re.compile(r'\((.*?)\)(?:,|$)')
    clean = line.strip()
    if clean.startswith(("(", " INSERT" )):
        m =p.findall(clean)
        #print "%s \t %s " %("1",clean)
        for i in m:
            print "%s" %(i)
