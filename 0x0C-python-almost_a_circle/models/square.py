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
        return "[Rectangle] ({}), {}/{} - {}/{}". format(self.id, self.x,
                                                         self.y, self.width,
                                                         self.height)
