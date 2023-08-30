#!/usr/bin/python3
"""define a class"""


class Square:
    """define a class square"""
    def __init__(self, size=0):
        """initialize an instance of the square with the attribute
        argument size being the value of the size of the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)
