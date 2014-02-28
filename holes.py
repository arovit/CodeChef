#!/usr/bin/python

import sys


def calculate(string):
    global_hash = {
'A' : 1,
'B' : 2,
'D' : 1,
'O' : 1,
'P' : 1,
'Q' : 1,
'R' : 1, 
}
    count = 0 
    for i in string:
        count += global_hash.get(i, 0)  
    return str(count) + '\n'

ntest = input()
for i in range(ntest):
    string =  sys.stdin.readline()
    sys.stdout.write(calculate(string)) 
   
