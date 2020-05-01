#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
    a, b = int(argv[1]), int(argv[3])
    signo = {"+": add, "-": sub, "/": div, "*": mul}
    if argv[2] not in signo:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {:d}"
          .format(argv[1], argv[2], argv[3], signo[argv[2]](a, b)))
