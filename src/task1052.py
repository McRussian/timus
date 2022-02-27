from typing import List, Tuple, Dict, Set


def most_common_number(ls: List[float]) -> int:
    key: Set[float] = set(ls)
    d: Dict[float, int] = dict()
    for k in key:
        d[k] = ls.count(k)
    return max(d.values())


def number_hares_on_line(points: List[Tuple[int, int]]) -> int:
    count: int = len(points)
    rez: Dict[Tuple[int, int], int] = dict()
    for i in range(count):
        rez[points[i]] = 0
        t: List[float] = list()
        for j in range(count):
            if j == i:
                continue
            try:
                t.append(round((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]), 6))
            except:
                t.append(100000000)
        rez[points[i]] = most_common_number(t) + 1
    return max(rez.values())


if __name__ == 'main':
    count = int(input())
    points: List[Tuple[int, int]] = list()
    for _ in range(count):
        points.append(tuple(map(int, input().split())))

    print(number_hares_on_line(points))
