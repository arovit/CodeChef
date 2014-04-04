#!/usr/bin/python

import sys
from collections import Counter

slist = sys.stdin.readlines()[1:]
for item in slist:
    print sum([int(value/ 2) + int(value % 2) for x, value in Counter(item.strip()).items()])
