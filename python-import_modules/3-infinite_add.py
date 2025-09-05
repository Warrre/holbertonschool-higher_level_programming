#!/usr/bin/python3

from sys import argv

total = 0

if __name__ == "__main__":
    for i in range(1, len(argv)):
        total += int(argv[i])
    print("{}".format(total))
