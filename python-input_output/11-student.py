#!/usr/bin/python3
"""Module for the Student class with selective JSON serialization."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dict of Student attributes.
        If attrs is a list of strings, only those attrs are returned.
        """
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
