#!/usr/bin/python3
"""
File: base.py

Author: Samson Tedla <samitedla23@gmail.com>

Defines a class called Base
"""
import json
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of objects to a file"""
        if list_objs is None:
            list_dict = []
        else:
            list_dict = []
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation"""
        json_list = []
        if json_string is None or len(json_string) == 0:
            return json_list
        else:
            json_list = (json.loads(json_string))
            return json_list

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance by processing a dictionary"""
        li = []
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file"""
        filename = cls.__name__ + ".csv"
        content = ""
        text = []
        if list_objs is not None:
            content += ','.join(list_objs[0].to_dictionary().keys())
            content += '\n'
            for lst in list_objs:
                content += ','.join(
                    map(str, lst.to_dictionary().values())
                )
                content += '\n'

        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(content)

    @classmethod
    def load_from_file_csv(cls):
        """load from csv"""
        filename = cls.__name__ + ".csv"
        object_created = []

        with open(filename, 'r') as f:
            header = f.readline().replace('\n', '').split(',')
            for el in f.readlines():
                values = map(int, el.replace('\n', '').split(','))
                data = dict(zip(header, values))
                object_created.append(cls.create(**data))
        return object_created
