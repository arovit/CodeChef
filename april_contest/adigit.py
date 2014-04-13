#!/usr/bin/python

import sys
lines = sys.stdin.readlines()
digit, testcase = lines[0].split()
input_string = lines[1].rstrip()
digit = int(digit)
testcase = int(testcase)
dp_dict = dict()
for j in range(0,10):
    dp_dict[j] = dict()
    for uindex, k in enumerate(input_string):
        if uindex == 0:
            dp_dict[j][uindex] = 0
        else:
            dp_dict[j][uindex] = abs(j-int(input_string[uindex -1])) + dp_dict[j][uindex-1]
for i in lines[2:]:
    i = int(i.strip())
    print dp_dict[int(input_string[i-1])][i-1] 
