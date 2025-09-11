#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    new_set = set(my_list)
    for i in new_set:
        result += i
    return result
