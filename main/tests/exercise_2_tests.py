import unittest
from main.src.exercise_2 import *


class TestMyDict(unittest.TestCase):
    # print({type('abc'), type(5)})
    def test_my_dict(self):
        test_my_dict = MyDict({'int', 'str'})
        test_my_dict.__setitem__('one', 1)
        self.assertEqual(1, test_my_dict['one'])
