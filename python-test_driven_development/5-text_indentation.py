#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines
after each of these characters: '.', '?' and ':'.
"""

def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'.

    Args:
        text: The input string.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()
    i = 0

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":  # If special char, print 2 new lines
            print("\n\n", end="")
            # Skip all spaces after the character
            while (i + 1) < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
