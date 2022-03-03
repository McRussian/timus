from typing import List, Tuple, Dict, Set

from .lib import Point


def triangle_sqaure(A: Point, B: Point, C: Point) -> int:
    # x [a] * (y [b] - y [c]) + x [b] * (y [c] - y [a]) + x [c] * (y [a] - y [b])
    return A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y)


def number_hares_on_line(points: List[Point]) -> int:
    count: int = len(points)
    max_point: List[int] = list()

    for i in range(count - 2):
        for j in range(i + 1, count - 1):
            cnt: int = 2
            for k in range(j + 1, count):
                if triangle_sqaure(points[i], points[j], points[k]) == 0:
                    cnt += 1
            max_point.append(cnt)
    return max(max_point)


if __name__ == 'main':
    count = int(input())
    points: List[Point] = list()
    for _ in range(count):
        x, y = tuple(map(int, input().split()))
        points.append(Point(x=x, y=y))

    print(number_hares_on_line(points))
