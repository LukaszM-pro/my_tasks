import unittest
from main.src.exercise_4 import *


class TestGiveMeList(unittest.TestCase):
    def test_give_me_list(self):
        self.assertEqual([5], give_me_list())
        self.assertEqual([5], give_me_list([]))
        self.assertEqual([3], give_me_list([], 3))
        self.assertEqual([1, 2, 3, 4], give_me_list([1, 2, 3], 4))
        self.assertEqual([1, 2, 3, 5], give_me_list([1, 2, 3]))

class TestReturnEveryThirdArgumentFromList(unittest.TestCase):
    def test_return_every_third_element_from_list(self):
        self.assertEqual([3,6,9], return_every_third_element_from_list([1,2,3,4,5,6,7,8,9]))
        self.assertEqual([3], return_every_third_element_from_list([1,2,3,4,5]))
        self.assertEqual([], return_every_third_element_from_list([]))
        self.assertEqual([i*3+2 for i in range(3)], return_every_third_element_from_list(list(range(10))))

