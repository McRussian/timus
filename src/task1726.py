from typing import List, Tuple

if __name__ == '__main__':
    count: int = int(input())
    points: List[Tuple[int, int]] = list()
    for _ in range(count):
        points.append(tuple(map(int, input().split())))
    summa_distance: int = 0
    count_distance: int = 0

    for i in range(count - 1):
        for j in range(i + 1, count):
            summa_distance += abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            count_distance += 1

    print(summa_distance//count_distance)
