#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = len(argv) - 1
    print("{:d} {:s}{:s}".format(number,
                                 "argument" if number <= 2 and number == 1
                                 else "arguments",
                                 "." if number == 0 else ":"))
    for a, b in enumerate(argv):
        if a > 0:
            print("{}: {}".format(a, b))
