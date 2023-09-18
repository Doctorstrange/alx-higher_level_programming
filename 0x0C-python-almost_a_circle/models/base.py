#!/usr/bin/python3
""" the first class Base"""
import json

class Base:
    """the “base” of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries:
        Return: the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """class Base by adding the class method def save_to_file(cls,
        list_objs): that writes the JSON string representation
        of list_objs to a file:
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dic_list = []
                for o in list_objs:
                    dic_list.append(o.to_dictionary())
                jsonfile.write(Base.to_json_string(dic_list))
