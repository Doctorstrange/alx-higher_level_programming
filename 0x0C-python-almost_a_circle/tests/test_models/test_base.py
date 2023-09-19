#!/usr/bin/python3
"""unitest for base.py"""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class Testto_json_string(unittest.TestCase):
    """unittest for json_string"""
    def test_empty_list(self):
        # Test when the input list is empty
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_none_input(self):
        # Test when the input is None
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_valid_input(self):
        # Test with a valid list of dictionaries
        data = [
            {"name": "femi", "age": 31},
            {"name": "ashley", "age": 28},
        ]
        expected_json = json.dumps(data)

        result = Base.to_json_string(data)
        self.assertEqual(result, expected_json)

    def square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        dic_list = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dic_list)) == 78)

if __name__ == '__main__':
    unittest.main()
