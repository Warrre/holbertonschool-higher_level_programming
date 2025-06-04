#!/usr/bin/python3
"""
student

this module contains
Student class
"""


class Student:
    """
    this class contains 2 methods:
    init to create an instance of this class,
    to_json to return a dictionary representation
    of a student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if all(isinstance(attr, str) for attr in attrs):
            new_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    new_dict[attr] = self.__dict__.get(attr)
            return new_dict
        else:
            return self.__dict__
