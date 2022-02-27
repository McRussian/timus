from tools import create_random_list
from random import randint
from unittest import TestCase

from src import binary_search

class TestTask1613(TestCase):
    def test_binary_search(self):
        for _ in range(100):
            ls = sorted(create_random_list(1000, 1000, 1100))
            self.assertEqual(binary_search(ls, 0, 1000, 100), -1)
            value = randint(1000, 1100)
            if value in ls:
                self.assertEqual(ls.index(value), binary_search(ls, 0, 1000, value))
            else:
                self.assertEqual(binary_search(ls, 0, 1000, value), -1)
