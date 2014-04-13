#!/usr/bin/python

import sys
import math



def is_prime(num):
    if (num % 2) == 0:
        return False 
    for i in range(2,int(math.sqrt(num)+1)):
        if (num % i) == 0:
            return False
    return True 
    
def get_next_prime(n):
    while True:
        if is_prime(n):
            return n
        n += 1     

lines = sys.stdin.readlines()
for num in lines[1:]:
    num1, num2 = num.strip().split(' ')
    num1 = int(num1)
    num2 = int(num2) 
    print get_next_prime(num1 + num2 +1) - (num1 + num2)

