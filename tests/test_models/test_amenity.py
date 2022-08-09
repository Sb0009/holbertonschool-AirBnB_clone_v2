#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Test for Class"""

    def __init__(self, *args, **kwargs):
        """ Test for Class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test for Class"""
        new = self.value()
        self.assertEqual(type(new.name), str)
