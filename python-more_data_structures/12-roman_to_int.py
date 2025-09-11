#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    total_value = 0
    prev_value = 0
    for i in reversed(roman_string):
        current_value = roman_values.get(i, 0)
        if current_value >= prev_value:
            total_value += current_value
        else:
            total_value -= current_value
        prev_value = current_value
    return total_value
