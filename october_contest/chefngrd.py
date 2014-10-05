#!/usr/bin/python

import sys

ntest = sys.stdin.readline()
ntest = int(ntest)

for i in range(0, ntest):
   n, m = map(int, sys.stdin.readline().strip().split(' ')) 
   args = map(int, sys.stdin.readline().strip().split(' '))
   intial_counter = max(args)
   intial_sum = sum(args)
   while True: 
      level = intial_counter * n
      extra = level - intial_sum 
      if m == extra:
         print "Yes"
         break
      else:
         if m > extra:
            intial_counter = intial_counter + 1 
            continue
         else:
            print "No"
            break
