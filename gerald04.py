#!/usr/bin/python

import sys
import datetime

line = sys.stdin.readline().strip()
for i in range(int(line)):
    time1 = sys.stdin.readline().strip()
    time1 = datetime.datetime.strptime(time1, "%H:%M")
    time2 = sys.stdin.readline().strip()
    time2 = datetime.datetime.strptime(time2, "%H:%M")
    dist = int(sys.stdin.readline().strip())
    time_delta = ((time1 - time2).seconds)/60   # Diff between chef and gf
    first_way = time_delta + dist
    if time_delta >= (2*dist):
        second_way = time_delta 
    else:
        second_way = time_delta + (2*dist - time_delta)/2.0 
    print "%.1f %.1f"%(first_way, second_way)
