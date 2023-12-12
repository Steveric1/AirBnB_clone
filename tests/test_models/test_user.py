#!/usr/bin/python3

"""Define unittests for models/user
Unittest classess:
    TestUser_Initialization
    TestUser_Save
    TestUser_To_Dict
"""
import os
import unittest
import models
from datetime import datetime as dt
from time import sleep
from models.user import User


class TestUser_Initialization(unittest.TestCase):
    """Unittest for testing User Models"""

    def test_no_args_initialization(self):
        user = User()
        self.assertEqual(User, type(user))

    def test_new_inst_stored_objs(self):
        self.assertIn(User(), models.storage.all().values())

    def test_created_at_is_pub_d_time(self):
        self.assertEqual(dt, type(User().created_at))

    def test_updated_at_is_pub_d_time(self):
        self.assertEqual(dt, type(User().updated_at))

    def test_id_is_pub_str(self):
        self.assertEqual(str, type(User().id))

    def test_email_str(self):
        self.assertEqual(str, type(User().email))

    def test_password_str(self):
        self.assertEqual(str, type(User().password))

    def test_first_name_str(self):
        self.assertEqual(str, type(User().first_name))

    def test_last_name_str(self):
        self.assertEqual(str, type(User().last_name))

    def test_user_unique_id(self):
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1, user2)

    def test_user_created_at_diff_time(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)

    def test_user_updated_at_diff_time(self):
        user1 = User()
        sleep(0.05)
        user2 = User()
        self.assertLess(user1.updated_at, user2.updated_at)

    # def test_str_representation(self):
    #     d_t = dt.today()
    #     dt_repr = repr(dt)
    #     us = User()
    #     us.id = "3312345"
    #     us.created_at = us.updated_at = d_t
    #     usstr = us.__str__()
    #     self.assertIn("[User] (3312345)", usstr)
    #     self.assertIn("'id': '3312345'", usstr)
    #     self.assertIn("'created_at': " + dt_repr, usstr)
    #     self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_args_unused(self):
        user = User(None)
        self.assertNotIn(None, user.__dict__.values())

    def test_instantiation_with_kwargs(self):
        d_time = dt.today()
        dt_iso = d_time.isoformat()
        user = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, d_time)
        self.assertEqual(user.updated_at, d_time)

    # def test_instantiation_with_None_kwargs(self):
    #     with self.assertRaises(TypeError):
    #         User(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        d_time = dt.today()
        dt_iso = d_time.isoformat()
        user = User("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, d_time)
        self.assertEqual(user.updated_at, d_time)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

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
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_two_saves(self):
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        second_updated_at = user.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        user.save()
        self.assertLess(second_updated_at, user.updated_at)

    def test_save_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save_updates_file(self):
        user = User()
        user.save()
        userid = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(userid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_to_dict_contains_added_attributes(self):
        user = User()
        user.middle_name = "Alx"
        user.my_number = 98
        self.assertEqual("Alx", user.middle_name)
        self.assertIn("my_number", user.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        user = User()
        us_dict = user.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_to_dict_output(self):
        d_time = dt.today()
        user = User()
        user.id = "123456"
        user.created_at = user.updated_at = d_time
        to_dict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': d_time.isoformat(),
            'updated_at': d_time.isoformat()
        }
        self.assertDictEqual(user.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        user = User()
        self.assertNotEqual(user.to_dict(), user.__dict__)

    def test_to_dict_with_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)


if __name__ == "__main__":
    unittest.main()
