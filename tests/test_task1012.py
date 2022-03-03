from random import randint

from unittest import TestCase
from src import count_K_number


class TestTask1012(TestCase):
    @staticmethod
    def __dec_to_base(N, base) -> str:
        if not hasattr(TestTask1012.__dec_to_base, 'table'):
            TestTask1012.__dec_to_base.table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        x, y = divmod(N, base)
        return TestTask1012.__dec_to_base(x, base) + \
                        TestTask1012.__dec_to_base.table[y] if x else TestTask1012.__dec_to_base.table[y]

    @staticmethod
    def __exhaustive_search_solve(n: int, k: int) -> int:
        count: int = 0
        for digit in range(n ** k):
            raw = TestTask1012.__dec_to_base(digit, k)
            if len(raw) == n and '00' not in raw:
                count += 1
        return count

    def test_count_knumber(self):
        self.assertEqual(TestTask1012.__exhaustive_search_solve(2, 10), 90)
        self.assertEqual(count_K_number(2, 10), 90)
        self.assertEqual(count_K_number(3, 10), TestTask1012.__exhaustive_search_solve(3, 10))

        for _ in range(10):
            n: int = randint(3, 8)
            k: int = randint(2, 16)
            self.assertEqual(count_K_number(n, k), TestTask1012.__exhaustive_search_solve(n, k))
