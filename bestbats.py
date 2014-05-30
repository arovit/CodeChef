#!/usr/bin/python

import math
from collections import Counter

no_testcases = input()

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
    

for i in range(0, no_testcases):  # Get the no of testcases
    player_array = raw_input().strip().split(' ')  # Get player array
    max_player = input()   # Max players  
    count_players = Counter(player_array)
    top_players = sorted(count_players.keys(), key=int)[::-1][:max_player+1]
    sumt = 0
    for i in top_players:
        if (sumt + count_players[i]) > max_player:
            print nCr(count_players[i], max_player - sumt) 
            break
        else:
            sumt = sumt + count_players[i] 
    else:
        print 1
