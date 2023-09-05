#!/usr/bin/python3
"""Define a class rectangle."""


class Rectangle:
    """initialize the rectangle"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """for retrieveing the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve rhe value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """return a representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        recrep = []
        for i in range(self.__height):
            [recrep.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                recrep.append("\n")
        return ("".join(recrep))
