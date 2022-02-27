from typing import Dict, Set, List
from collections import defaultdict


# Returns index of x in arr if present, else -1
def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return -1


def in_ls(ls: List[int], value: int) -> bool:
    return not binary_search(ls, 0, len(ls), value) == -1


def get_statist(raw: str) -> Dict[int, Set[int]]:
    raw_stat: Dict[int, Set[int]] = defaultdict(set)
    for index, item in enumerate(map(int, raw.split())):
        raw_stat[item].add(index + 1)
    return {
        key: sorted(list(value)) for key, value in raw_stat.items()
    }


if __name__ == '__main__':
    k = int(input())
    raw = input()
    stat: Dict[int, Set[int]] = get_statist(raw)
    count = int(input())
    s = ''
    for _ in range(count):
        l, r, value = map(int, input().split())
        if not value in stat.keys():
            s += '0'
            continue
        for i in range(l, r + 1):
            if i in stat[value]:
                s += '1'
                break
        else:
            s += '0'
    print(s)
