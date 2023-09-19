#!/usr/bin/python3
"""unitest for base.py"""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestArea(unittest.TestCase):

    def testpositive_values(self):
        rectangle = Rectangle(2, 10)
        result = rectangle.area()
        self.assertEqual(result, 20)

    def testzero_values(self):
        rectangle = Rectangle(0, 0)
        result = rectangle.area()
        self.assertEqual(result, 0)

    def testnegative_values(self):
        rectangle = Rectangle(-2, 10)
        result = rectangle.area()
        self.assertEqual(result, -20)



if __name__ == '__main__':
    unittest.main()
