import unittest
from main.src.exercise_1 import *


class TestNMostFrequent(unittest.TestCase):
    def test_n_most_frequent(self):
        self.assertEqual({' ': 2, 'mama': 2, 'tata': 1}, most_frequent_n_words('tata mama mama'))
        self.assertEqual({' ': 4, 'bbb': 2}, most_frequent_n_words('aa aa aa bbb bbb'))
        self.assertEqual({' ': 11, 'ccc': 5}, most_frequent_n_words('aaa aaa aaa bbb bbb bbb bbb ccc ccc ccc ccc ccc', 2))
        self.assertEqual({' ': 15, 'aaa': 3, 'bbb': 3, 'ccc': 3, 'ddd': 3},
                         most_frequent_n_words('aaa aaa aaa bbb bbb bbb ccc ccc ccc ddd ddd ddd eee eee fff fff'))
