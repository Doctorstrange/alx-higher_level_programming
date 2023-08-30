#!/usr/bin/python3
"""define a class"""


class Square:
    """define a class square"""
    def __init__(self, size=0):
        """initialize an instance of the square with the attribute
        argument size being the value of the size of the square"""
        self.size = size

    @property
    def size(self):
        """retrieve size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
