#!/usr/bin/python3
import sys

n = len(sys.argv)

if n == 1:
    print('{} arguments.'.format(n - 1))
else:
    print('{} arguments:'.format(n - 1))
    for i in range(0, n - 1):
        print('{}'"."'{:s}'.format(i + 1, sys.argv[i + 1]))
