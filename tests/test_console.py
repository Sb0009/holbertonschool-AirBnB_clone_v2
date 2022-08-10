#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
import os
from io import StringIO
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def create(self):
        ''' create an instance of the HBNBCommand class'''
        return HBNBCommand()

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.count.__doc__)
        self.assertIsNotNone(HBNBCommand.strip_clean.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_create(self):
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd("create User")
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            with patch('sys.stdout', new=StringIO()) as f:
                self.consol.onecmd(
                    'create User \
                     email="abc@def.com" \
                     password="123456" \
                     first_name="Julanito" \
                     last_name="Redondo" \
                     ')
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create State name="Bogota"\
            lat=7.5 zip=110151')
            id = f.getvalue().strip("\n")
        alldic = storage.all()
        clas = "State."
        Sname = alldic[clas + id].name
        Slat = alldic[clas + id].lat
        Szip = alldic[clas + id].zip
        self.assertEqual(Sname, "Bogota")
        self.assertTrue(isinstance(Sname, str))
        self.assertEqual(Slat, 7.5)
        self.assertTrue(isinstance(Slat, float))
        self.assertEqual(Szip, 1101051)
        self.assertTrue(isinstance(Szip, int))

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

if __name__ == "__main__":
    unittest.main()
