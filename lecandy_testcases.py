#! /usr/bin/python

import random
import sys

def generate_testcases():
    number = 100000000
    print number
    for i in xrange(0,number):
        N = 100
        C = random.randint(100000000, 1000000000000000000000)
        print "%s %s"%(N, C)
        print ' '.join([str(random.randint(10000000, 100000000000)) for i in range(0,N)])

generate_testcases()
