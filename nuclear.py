#!/usr/bin/python

import sys

lines = sys.stdin.readlines()[0].strip()
A, N, K = map(int, lines.split(' '))
for i in range(K):
    sys.stdout.write(str(A%(N+1)) + ' ')
    A = A/(N+1)
