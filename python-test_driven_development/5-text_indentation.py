#!/usr/bin/python3
"""
Function that prints a text with two new lines after '.', '?', and ':'.
"""


def text_indentation(text):
    """Prints a text with two new lines after '.', '?', and ':'."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    buffer = ""
    for c in text:
        if c in ('.', '?', ':'):
            buffer += c
            print(buffer.strip())
            print()
            buffer = ""
        elif c == '\n':
            if buffer.strip():
                print(buffer.strip())
            print()
            buffer = ""
        else:
            buffer += c

    if buffer.strip():
        print(buffer.strip(), end="")
