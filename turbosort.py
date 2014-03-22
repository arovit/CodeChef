#!/usr/bin/python

import sys

lines = sys.stdin.readlines()[1:]
print ' '.join(sorted(lines , key=int))
