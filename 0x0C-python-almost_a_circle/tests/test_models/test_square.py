#!/usr/bin/python3
"""unitest for base.py"""

import json
import unittest
from models.base import Base
from models.square import Square

class TestUpdate(unittest.TestCase):
    def testsetup(self):
        self.square = Square(1)



if __name__ == '__main__':
    unittest.main()
