#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each of
    these characters:
    ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()

    i = 0
    while i < len(text):
        if i == 0 and text[i] == ' ':
            i += 1
            continue

        print(text[i], end="")

        if text[i] in ".?:":
            print("\n\n", end="")
            while (i + 1) < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
