#!/usr/bin/python

import sys

def main():
    t = int(sys.stdin.readline().strip())
    for i in range(t):
        A, C = sys.stdin.readline().strip().split(' ')
        A = int(A)
        C = int(C)
        add = reduce(lambda x, y: int(x) + int(y), sys.stdin.readline().strip().split(' ') , 0)
        if add <= C:
            sys.stdout.write("Yes"+'\n')
        else:
            sys.stdout.write("No"+'\n')

if __name__ == "__main__":
    main()
