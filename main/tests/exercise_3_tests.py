import unittest
from main.src.exercise_3 import *

class TestIsPalindrome(unittest.TestCase):
    def test_give_me_list(self):
        self.assertEqual(True, is_palindrome('1221'))
        self.assertEqual(True, is_palindrome('121'))
        self.assertEqual(False, is_palindrome('12'))
        self.assertEqual(True, is_palindrome('0'))


class TestCountPalindromes(unittest.TestCase):
    def test_count_palindromes_per_give_string_lenght(self):
        self.assertEqual(1, count_palindromes_per_give_string_length('1221', 10))
        self.assertEqual(1, count_palindromes_per_give_string_length('121', 10))
        self.assertEqual(0, count_palindromes_per_give_string_length('12', 10))
        self.assertEqual(1, count_palindromes_per_give_string_length('0', 10))
        self.assertEqual(2, count_palindromes_per_give_string_length('1221\n2222\n3223', 9))


class TestCountPalindromesFromFile(unittest.TestCase):
    def test_count_palindromes_per_give_string_length_in_file(self):
        self.assertEqual(4, count_palindromes_per_give_string_length_in_file('palindrome_test.txt', 10))
