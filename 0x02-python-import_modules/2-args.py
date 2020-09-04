#!/usr/bin/python3
import sys

n = len(sys.argv)

if n == 1:
    print('{} arguments.'.format(n - 1))
else:
    print('{} arguments:'.format(n - 1))
    for i in range(1, n):
        print('{}'": "'{:s}'.format(i, sys.argv[i]))
