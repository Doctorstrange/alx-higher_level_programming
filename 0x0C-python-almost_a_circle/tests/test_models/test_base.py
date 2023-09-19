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

    def testsquare_two_dicts(self):
        s1 = Square(8, 3, 4, 2)
        s2 = Square(5, 7, 2, 8)
        dic_list = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dic_list)) == 76)

class TestSaveToFile(unittest.TestCase):

    def test_empty_list(self):
        empty_list = []
        Base.save_to_file(empty_list)

        with open("Base.json", "r") as jsonfile:
            content = jsonfile.read()
            self.assertEqual(content, "[]")

    def testfile_with_data(self):
        class ExampleObject:
            def __init__(self, name):
                self.name = name

            def to_dictionary(self):
                return {"name": self.name}

        data = [ExampleObject("femi"), ExampleObject("ashley")]
        Base.save_to_file(data)

        with open("Base.json", "r") as jsonfile:
            content = jsonfile.read()
            expected_json = json.dumps([{"name": "femi"}, {"name": "ashley"}])
            self.assertEqual(content, expected_json)


if __name__ == '__main__':
    unittest.main()
