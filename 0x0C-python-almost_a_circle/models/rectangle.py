#!/usr/bin/python3
""" the class Rectangle that inherits from Base"""
from models.base import Base

class Rectangle(Base):
    """ the class Rectangle that inherits from Base"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Private instance attributes, each with its
        own public getter and setter
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for private attribute __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set the width value for private attribute __width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for the y attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height
