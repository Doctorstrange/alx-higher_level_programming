#!/usr/bin/python3
"""the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for value size"""
        return self.width

    @size.setter
    def size(self, value):
        """to set the width and height value for private attribute size"""
        self.width = value
        self.height = value

    def __str__(self):
        """returns [square] (<id>) <x>/<y> - <width>/<height>
        Return: [square] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}". format(self.id, self.x,
                                                      self.y, self.size,
                                                      )

    def update(self, *args, **kwargs):
        """Update the class Square by adding the public method def
        update(self, *args, **kwargs) that assigns attributes:

        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """

        if len(args) != 0:
            for ele in args:
                if ele == 0:
                    self.id = ele
                if ele == 1:
                    self.size = ele
                if ele == 2:
                    self.x = ele
                if ele == 3:
                    self.y == ele

        elif kwargs != 0:
            for key, ele in kwargs.items():
                if key == "id":
                    self.id = ele
                if key == "size":
                    self.size = ele
                if key == "x":
                    self.x = ele
                if key == "y":
                    self.y = ele

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle:
        Return: returns the dictionary representation of a Rectangle:
        """
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
