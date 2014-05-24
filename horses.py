#!/usr/bin/python

n_tests = input()

for i in range(0,n_tests):
    N = input()
    S = raw_input().strip().split(' ')
    S = sorted(S, key=int)
    mini = 1000000000000000000000000   # Very high number initial
    rev = S[::-1]
    for indx, j in enumerate(rev):
        try:
            diff = int(rev[indx]) - int(rev[indx + 1])
            if mini > diff:
                mini = diff 
        except IndexError:
            pass
    print mini
