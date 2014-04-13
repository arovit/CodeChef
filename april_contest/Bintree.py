#!/usr/bin/python

import sys
import math

cache_parent = {}
       
def find_chain_1(num1, parent_c1): 
    while True:
        if cache_parent.has_key(num1):
            parent_c1.extend(cache_parent[num1])
            return parent_c1
        parent_c1.append(num1)
        if num1 == 1:
            return
        num1 = int(num1/2)

def find_chain_2(num2, parent_c2): 
    while True:
        if cache_parent.has_key(num2):
            parent_c2.extend(cache_parent[num2])
            return parent_c2
        parent_c2.append(num2)
        if num2 == 1:
            return
        num2 = int(num2/2)
  
def getlen(chain_1, chain_2, num1, num2):
    """if len(chain_1) > len(chain_2):
        shorter = chain_2
        larger = chain_1
    else:
        shorter = chain_1
        larger = chain_2
    for i in shorter:
        if i in larger:
            root = i
            break"""
    root = list(set(chain_1) & set(chain_2))
    root.sort()
    root = root[-1]
    #distance = int(math.log(num1, 2) + 1) + int(math.log(num2, 2) + 1)   - 2*int(math.log(root, 2)+1)
    #print root
    distance = chain_1.index(root) + chain_2.index(root)
    return distance

lines = sys.stdin.readlines()
for num in lines[1:]:
    num1, num2 = num.strip().split(' ')
    num1 = int(num1)
    num2 = int(num2) 
    parent_c1 = []  
    parent_c2 = []
    find_chain_1(num1, parent_c1)
    cache_parent[num1] = parent_c1
    #print parent_c1 
    find_chain_2(num2, parent_c2)
    cache_parent[num2] = parent_c2
    #print parent_c2
    print getlen(parent_c1, parent_c2, num1, num2)
