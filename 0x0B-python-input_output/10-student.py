#!/usr/bin/python3
"""Write a class Student that defines a student by"""


class Student:
    """Write a class Student that defines a student by"""

    def __init__(self, first_name, last_name, age):
        """Write a class Student that defines a student by
    Return: retrieves a dictionary representation of a Student instance
    """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance
        Return: str
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {f: getattr(self, f) for f in attrs if hasattr(self, f)}
        return self.__dict__
