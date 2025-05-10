#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 1:
        print("0 arguments.")
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
