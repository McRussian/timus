from random import randint
from unittest import TestCase

from src import count_good_number, is_square, is_pow

class TestTask2070(TestCase):
    def test_is_square(self):
        for _ in range(10000000):
            value = randint(10, 10000000)
            self.assertTrue(is_square(value ** 2))
            self.assertFalse(is_square(value ** 2 + 1))
            self.assertFalse(is_square(value ** 2 - 1))

    def test_is_pow(self):
        pows = [2, 4, 6, 10, 12]
        for _ in range(10000):
            value = randint(10, 10000000)
            for pow in pows:
                self.assertTrue(is_pow(value ** pow, pow))
                self.assertTrue(is_pow(value ** pow, pow + 1))
                self.assertTrue(is_pow(value ** pow, pow - 1))

    def test_count_good_number(self):
        self.assertEqual(count_good_number(3, 7), 4)
        self.assertEqual(count_good_number(2, 2), 1)
        self.assertEqual(count_good_number(77, 1010), 924)
        self.assertEqual(count_good_number(1000, 100000000000), 99999971585)
        self.assertEqual(count_good_number(10, 100), 86)
        self.assertEqual(count_good_number(17, 500), 476)
