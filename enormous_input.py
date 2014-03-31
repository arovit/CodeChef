#! /usr/bin/python

import sys
stdin = sys.stdin

count = 0 
input_n = map(int, stdin.readline().split())
n = input_n[0]
k = input_n[1]
if k%2 == 0: 
    even = 1
else:
    even = 0 
idx = 0 
while idx < n:
    no = int(stdin.readline()) 
    if no >= k:
        if even:
            if (no & 1 == 0) and no%k == 0:
                count+=1 
        else:
            if no%k == 0:
                count+=1
    idx+=1
print count    
