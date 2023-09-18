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
        if type(value) is not int:
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
        if not isinstance(value, int):
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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character
        # - you don’t need to handle x and y here."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for y in range(self.width)]
            print("")

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        Return: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}), {}/{} - {}/{}". format(self.id, self.x,
                                                         self.y, self.width,
                                                         self.height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute:"""
        if len(args) != 0:
            count = 0
            for ele in args:
                if count == 0:
                    self.id = ele
                if count == 1:
                    self.width = ele
                if count == 2:
                    self.height = ele
                if count == 3:
                    self.x = ele
                if count == 4:
                    self.y = ele
                count += 1

        elif len(kwargs) != 0:
            for key, ele in kwargs.items():
                if key == "id":
                    self.id = ele
                if key == "width":
                    self.width = ele
                if key == "height":
                    self.height = ele
                if key == "x":
                    self.x = ele
                if key == "y":
                    self.y = ele

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:
        Return: returns the dictionary representation of a Rectangle:
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
