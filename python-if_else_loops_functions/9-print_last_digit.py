#!/usr/bin/python3
def print_last_digit(number):
    last = abs(number) % 10
    if last < 0:
        last = -last
    print(last, end="")
    return last
