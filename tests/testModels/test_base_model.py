#!/usr/bin/python3

"""Define unittest for models/base_model.py
Unittest Classes:
    TestBaseModel_initialization
"""
import os
import models
import unittest
from datetime import datetime as d_time
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_initialization(unittest.TestCase):
    """Unittest for testing initialization of BaseModel"""
    
    def test_no_args_initialization(self):
        self.assertEqual(BaseModel, type(BaseModel()))
        
    def test_new_inst_stored_objs(self):
        self.assertIn(BaseModel(), models.storage.all().values())
        
    def test_created_at_is_pub_d_time(self):
        self.assertEqual(d_time, type(BaseModel().created_at))
        
    def test_updated_at_is_pub_d_time(self):
        self.assertEqual(d_time, type(BaseModel().updated_at))
        
    def test_id_is_pub_str(self):
        self.assertEqual(str, type(BaseModel().id))
    
    def test_unique_id(self):
        B_model_1 =  BaseModel()
        B_model_2 = BaseModel()
        self.assertNotEqual(B_model_1, B_model_2)
    
    def test_two_model_diff_created_at(self):
        B_model_1 = BaseModel()
        sleep(0.05)
        B_model_2 = BaseModel()
        self.assertLess(B_model_1.created_at, B_model_2.created_at)
    
    def test_two_model_diff_updated_at(self):
        B_model_1 = BaseModel()
        sleep(0.05)
        B_model_2 = BaseModel()
        self.assertLess(B_model_1.updated_at, B_model_2.updated_at)
        
    def test_str_repr(self):
        dt = d_time.today()
        d_repr = repr(dt)
        b_model = BaseModel()
        b_model.created_at = b_model.updated_at = dt
        b_model.id = "3312345"
        Bmodel_str = b_model.__str__()
        self.assertIn("[BaseModel] (3312345)", Bmodel_str)
        self.assertIn("'id': '3312345'", Bmodel_str)
        self.assertIn("'created_at': " + d_repr, Bmodel_str)
        self.assertIn("'updated_at': " + d_repr, Bmodel_str)
    
    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = d_time.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    # def test_instantiation_with_None_kwargs(self):
    #     with self.assertRaises(TypeError):
    #         BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = d_time.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = d_time.today()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()