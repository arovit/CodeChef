#!/usr/bin/python

import sys

global_hash = {
}


def factorial(n):
    if n <= 1:
        return 1
    hashv = global_hash.get(n, None)
    if hashv:
        return hashv
    else:
        global_hash[n] = n * factorial(n-1)
        return global_hash[n]

lines = sys.stdin.readlines()
for i in range(int(lines[0])):
    sys.stdout.write(str(factorial(int(lines[i+1]))) + ' ') 
