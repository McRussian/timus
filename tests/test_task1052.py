from random import randint
from typing import List, Set, Tuple
from unittest import TestCase
from src import number_hares_on_line, Point


class TestTask1052(TestCase):
    def test_number_hares_on_line(self):
        points: List[Point] = [
            Point(7, 122),
            Point(8, 139),
            Point(9, 156),
            Point(10, 173),
            Point(11, 190),
            Point(-100, 1),
        ]
        self.assertEqual(number_hares_on_line(points), 5)
        points = [
            Point(-98, -1368),
            Point(352, -1057),
            Point(-309, -4322),
            Point(338, -1015),
            Point(-337, -4714),
            Point(-458, 1373),
            Point(262, 3672),
            Point(392, -1177),
            Point(-92, -1284),
            Point(-43, 128),
            Point(-453, -6338),
            Point(-412, -5764),
            Point(20, -61),
            Point(52, 732),
            Point(-164, 491),
            Point(485, 6794),
            Point(-83, 248),
            Point(196, 2748),
            Point(-130, 389),
            Point(63, 886),
            Point(-334, 1001),
            ]
        self.assertEqual(number_hares_on_line(points), 11)

    def test_singleline(self):
        count_test: int = randint(50, 100)
        for _ in range(count_test):
            line: Tuple[int, int] = randint(0, 40) - 20, randint(0, 40) - 20
            count_point: int = randint(10, 25)
            points: Set[Point] = set()
            for __ in range(count_point):
                x: int = randint(0, 1000) - 500
                y: int = line[0] * x + line[1]
                points.add(Point(x, y))
            self.assertEqual(number_hares_on_line(list(points)), count_point)

    def test_two_line(self):
        count_test: int = 25
        for _ in range(count_test):
            line1: Tuple[int, int] = randint(0, 40) - 20, randint(0, 40) - 20
            line2: Tuple[int, int] = randint(0, 40) - 20, randint(0, 40) - 20
            count_point: int = randint(5, 12)
            points: Set[Point] = set()
            for __ in range(count_point):
                x1: int = randint(0, 1000) - 500
                y1: int = line1[0] * x1 + line1[1]
                points.add(Point(x1, y1))
                x2: int = randint(0, 1000) - 500
                y2: int = line2[0] * x2 + line2[1]
                points.add(Point(x2, y2))
            if number_hares_on_line(list(points)) != count_point:
                print(f"Line1: {line1}")
                print(f"Line2: {line2}")
                print(list(map(str, points)))
            self.assertEqual(number_hares_on_line(list(points)), count_point)

    def test_random_data(self):
        count_line: int = 5
        lines: List[Tuple[int, int]] = [
            (randint(0, 40) - 20, randint(0, 40) - 20) for _ in range(count_line)
        ]

        points: Set[Point] = set()
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
                    points.add(Point(x, y))
                    current_point += 1

        self.assertEqual(number_hares_on_line(list(points)), max_point)
