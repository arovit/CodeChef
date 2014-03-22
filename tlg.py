#!/usr/bin/python

import sys

@profile
def main():
  total1 = 0
  total2 = 0
  player = 0
  max_lead = 0
  lines = sys.stdin.readlines()
  for i in xrange(int(lines[0])):
    player1, player2 = lines[i+1].split(' ')
    total1 = total1  +  int(player1)
    total2 = total2 + int(player2)
    lead1 = total1 - total2
    lead2 = total2 - total1
    if lead1 > lead2 and lead1 > max_lead:
      max_lead = lead1
      player = '1 '
    elif lead2 > lead1 and lead2 > max_lead:
      max_lead = lead2
      player = '2 '
  sys.stdout.write(player + str(max_lead) + '\n')

if __name__ == "__main__":
  main()
