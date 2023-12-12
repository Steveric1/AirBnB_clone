#!/usr/bin/python3

"""Define unittests for models/user
Unittest classess:
    TestState_Initialization
    TestState_Save
    TestState_To_Dict
"""
import os
import unittest
import models
from datetime import datetime as dt
from time import sleep
from models.state import State


class TestUser_Initialization(unittest.TestCase):
    """Unittest for testing User Models"""

    def test_no_args_initialization(self):
        state = State()
        self.assertEqual(State, type(state))

    def test_new_inst_stored_objs(self):
        self.assertIn(State(), models.storage.all().values())

    def test_created_at_is_pub_d_time(self):
        self.assertEqual(dt, type(State().created_at))

    def test_updated_at_is_pub_d_time(self):
        self.assertEqual(dt, type(State().updated_at))

    def test_id_is_pub_str(self):
        self.assertEqual(str, type(State().id))

    def test_name_is_public_class_attribute(self):
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(st))
        self.assertNotIn("name", st.__dict__)

    def test_state_unique_id(self):
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1, state2)

    def test_state_created_at_diff_time(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.created_at, state2.created_at)

    def test_user_updated_at_diff_time(self):
        state1 = State()
        sleep(0.05)
        state2 = State()
        self.assertLess(state1.updated_at, state2.updated_at)

    # def test_str_representation(self):
    #     d_t = dt.today()
    #     dt_repr = repr(dt)
    #     state = State()
    #     state.id = "3312345"
    #     state.created_at = state.updated_at = d_t
    #     st_str = state.__str__()
    #     self.assertIn("[User] (3312345)", st_str)
    #     self.assertIn("'id': '3312345'", st_str)
    #     self.assertIn("'created_at': " + dt_repr, st_str)
    #     self.assertIn("'updated_at': " + dt_repr, st_str)

    def test_args_unused(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_instantiation_with_kwargs(self):
        d_time = dt.today()
        dt_iso = d_time.isoformat()
        state = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, d_time)
        self.assertEqual(state.updated_at, d_time)

    # def test_instantiation_with_None_kwargs(self):
    #     with self.assertRaises(TypeError):
    #         State(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        d_time = dt.today()
        dt_iso = d_time.isoformat()
        state = State("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, d_time)
        self.assertEqual(state.updated_at, d_time)


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
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)

    def test_two_saves(self):
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        second_updated_at = state.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        state.save()
        self.assertLess(second_updated_at, state.updated_at)

    def test_save_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_save_updates_file(self):
        state = State()
        state.save()
        stid = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(stid, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_to_dict_contains_added_attributes(self):
        state = State()
        state.middle_name = "Alx"
        state.my_number = 98
        self.assertEqual("Alx", state.middle_name)
        self.assertIn("my_number", state.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        state = State()
        st_dict = state.to_dict()
        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["created_at"]))
        self.assertEqual(str, type(st_dict["updated_at"]))

    def test_to_dict_output(self):
        d_time = dt.today()
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = d_time
        to_dict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': d_time.isoformat(),
            'updated_at': d_time.isoformat()
        }
        self.assertDictEqual(state.to_dict(), to_dict)

    def test_contrast_to_dict_dunder_dict(self):
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_to_dict_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)


if __name__ == "__main__":
    unittest.main()
