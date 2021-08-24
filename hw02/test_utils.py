#!/usr/bin/env python3

import unittest
from utils import validate_json_file

class TestUtilsJSONFile(unittest.TestCase):

    def test_get_num_animals(self):
        self.assertRaises(AssertionError, validate_json_file, 'invalidstring')
        self.assertRaises(AssertionError, validate_json_file, 'wrong_file_type.txt')
        self.assertRaises(AssertionError, validate_json_file, 33)
        self.assertEqual(validate_json_file('valid.json'), None)

if __name__ == '__main__':
    unittest.main()
