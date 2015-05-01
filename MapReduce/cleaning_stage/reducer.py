#!/usr/bin/python

import sys


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    key,something = line.strip().split("\t")
    print "%s\t%s" %(key, "")

