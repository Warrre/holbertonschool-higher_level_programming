#!/usr/bin/python3
"""
pascal_triangle

this function recreate
the n élément of pascal triangle
"""


def pascal_triangle(n):
    """
    this function create the pascal triangle
    and return a list of lists of integers
    representing it
    """
    if n <= 0:
        return []
    pascal = []
    for i in range(n):
        pascal_j = []
        for j in range(i + 1):
            if j == 0 or j == i:
                pascal_j.append(1)
            else:
                pascal_j.append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal.append(pascal_j)
    return pascal
