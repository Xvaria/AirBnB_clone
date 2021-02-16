#!/usr/bin/python3
'''Test to the BaseModel class'''

from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    '''Test cases to the BaseModel class'''

    def test_id(self):
        '''Test the correct id assignment'''
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.id, b.id)

    def test_datastored(self):
        '''Test the data type stored in the object'''
        test2 = BaseModel()
        self.assertEqual(type(test2.id), str)
        self.assertEqual(type(test2.created_at), datetime.datetime)
        self.assertEqual(type(test2.updated_at), datetime.datetime)

    def test_to_dic(self):
        '''Test the correct output of the 'to_dic' method'''
        test3 = BaseModel()
        dic = test3.to_dict()
        self.assertEqual(len(dic), 4)
        test3.name = 'John'
        dic = test3.to_dict()
        self.assertEqual(len(dic), 5)
        test3.last_name = 'Wick'
        dic = test3.to_dict()
        self.assertEqual(len(dic), 6)
        for i in dic.values():
            self.assertEqual(type(i), str)

    def test_from_dic(self):
        '''Test the generation of a object from a dic'''
        a = BaseModel()
        dic = a.to_dict()
        b = BaseModel(dic)
        self.assertNotEqual(a, b)
        self.assertEqual(type(b.created_at), datetime.datetime)
        self.assertEqual(type(b.updated_at), datetime.datetime)

    def test_str(self):
        ''' Testing str '''
        model = BaseModel()
        string = "[{}] ({}) {}".format(model.__class__.__name__, model.id,
                                       model.__dict__)
        self.assertEqual(str(model), string)

    def test_to_dict_method(self):
        """ Check """
        model = BaseModel()
        model.name = "Holberton"
        model.my_number = 89
        model.my_float = 100.54
        model.my_list = ["Hello", "world", 100]
        model.my_dict = {'name': 'Betty', 'last_name': 'Holberton', 'age': 85}
        model.save()
        model_json = model.to_dict()
        # checks if the method really convert to a dict type all the attributes
        self.assertEqual(type(model_json), dict)
        for key, value in model_json.items():
            # checks if the dict has the same attributes keys that the object
            self.assertTrue(hasattr(model, key))
            # checks if datetime was safe as a iso format and its type
            if key == "created_at" or key == "updated_at":
                _datetime = getattr(model, key).isoformat()
                self.assertEqual(_datetime, value)
                self.assertTrue(type(value) == str)
            elif key == "__class__":
                self.assertEqual(model.__class__.__name__, value)
                self.assertTrue(type(value) == str)
            else:
                self.assertEqual(getattr(model, key), value)
                if key == "id":
                    version = uuid.UUID(value).version
                    self.assertEqual(version, 4)
                    self.assertTrue(type(value), str)
                elif key == "name":
                    self.assertTrue(type(value) == str)
                elif key == "my_number":
                    self.assertTrue(type(value) == int)
                elif key == "my_list":
                    self.assertTrue(type(value) == list)
                elif key == "my_float":
                    self.assertTrue(type(value) == float)
                elif key == "my_dict":
                    self.assertTrue(type(value) == dict)
