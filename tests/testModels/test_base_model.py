#!/usr/bin/python3

"""Define unittest for models/base_model.py
Unittest Classes:
    TestBaseModel_initialization
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_initialization(unittest.TestCase):
    """Unittest for testing initialization of BaseModel"""
    
    def test_no_args_initialization(self):
        self.assertEqual(BaseModel, type(BaseModel()))
