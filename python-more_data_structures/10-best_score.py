#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_score = max(a_dictionary, key=a_dictionary.get)
        return max_score
    return None
