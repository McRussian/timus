from random import randint
from typing import List, Set, Tuple
from unittest import TestCase
from src import number_hares_on_line


class TestTask1052(TestCase):
    def test_number_hares_on_line(self):
        points: List[Tuple[int, int]] = [
            (7, 122),
            (8, 139),
            (9, 156),
            (10, 173),
            (11, 190),
            (-100, 1),
        ]
        self.assertEqual(number_hares_on_line(points), 5)

    def test_random_data(self):
        count_line: int = 150
        lines: List[Tuple[int, int]] = [
            (randint(0, 40) - 20, randint(0, 40) - 20) for _ in range(count_line)
        ]

        points: Set[Tuple[int, int]] = set()
        max_point: int = 0
        for i in range(len(lines)):
            count_point: int = randint(1, 13)
            if count_point > max_point:
                max_point = count_point
            current_point: int = 0
            while current_point < count_point:
                x: int = randint(0, 1000) - 500
                y: int = lines[i][0] * x + lines[i][1]
                for j in range(i):
                    if y == lines[j][0] * x + lines[j][1]:
                        break
                else:
                    points.add((x, y))
                    current_point += 1
            self.assertEqual(number_hares_on_line(list(points)), max_point)

        self.assertEqual(number_hares_on_line(list(points)), max_point)
