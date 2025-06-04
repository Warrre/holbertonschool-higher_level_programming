#!/usr/bin/python3
"""Module for CustomObject"""
import pickle


class CustomObject:
    """A custom object class"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object to a file"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize the object from a file"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
