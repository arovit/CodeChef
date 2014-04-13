#!/usr/bin/python

import itertools
import sys

cache = {}
combinations_cache = {}
def primes(n):
    global cache
    primfac = list()
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
            if cache.has_key(n):
                primfac.extend(cache[n])
                return primfac
        d += 1
    if n > 1: 
        primfac.append(n)
    return primfac
  
def determinants(n):
    global cache
    global combinations_cache
    if not cache.has_key(n):
        cache[n] = primes(n)
    if n == 1:
        return 1
    #print cache[n]
    if len(set(cache[n])) == 1:
        # If power of prime or prime number itself
        if cache[n][0] != n:
            if len(cache[n]) % 2 == 0:
                return (int(len(cache[n])/2)*2 + 1)
            else:
                return (int(len(cache[n])/2)*2 + 2)
        else:
            return 2
    else:
        tot_set = 0
        cache[n].sort()  
        rlimit = int(len(cache[n]))
        #print rlimit
        for j in range(1, rlimit):
            tot_set = tot_set + len(set(i for i in itertools.combinations(cache[n], j)))
            #print c
        return tot_set + 2
        
lines = sys.stdin.readlines()[1:]
global cache_deter
cache_deter = {}
cache_deter_over = {}
for line in lines:
    trace = int(line.strip())
    tot_ways = 0
    uplimit = int(trace/2)
    if trace == 1 or trace == 2:
        print 0  
        continue
    for i in range(1, uplimit+1):
        x = i
        y = trace - i 
        #print x, y
        coms = 0
        mul = x*y 
        if cache_deter_over.has_key(mul):
            coms = cache_deter_over[mul]
        else:
            for k in range(1, mul):
                if cache_deter.has_key(k):
                    #print ' HIT %s'%k
                    val = cache_deter[k] 
                else:
                    val =  determinants(k)
                    cache_deter[k] = val
 
                #print ' deter %s'%k
                #print 'value %s'%val
                coms += val
                #print coms
            cache_deter_over[mul] = coms
        #print coms
        if x != y:
            tot_ways = tot_ways + (2 * coms)
        else:
            tot_ways = tot_ways + coms 
    print tot_ways
#print cache_deter
