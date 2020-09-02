#!/usr/bin/python3
for alpharev in range(ord('z'), ord('a') - 1, -1):
    if alpharev % 2 == 1:
        alpharev = alpharev - 32
    print("{:s}".format(chr(alpharev)), end="")
