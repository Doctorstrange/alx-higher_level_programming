#!/usr/bin/python3
"""geometry class BaseGeometry."""


class BaseGeometry:
    """base geometry."""

    def area(self):
        """raise"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
