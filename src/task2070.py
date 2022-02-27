def is_square(num: int) -> bool:
    root = int(num ** 0.5)
    return root ** 2 == num


def is_pow(num: int, p: int) -> bool:
    root = int(num ** (1 / p))
    return root ** p == num


def count_square(left: int, right: int) -> int:
    return len(list(filter(is_square, range(left, right + 1))))


def count_good_number(left: int, right: int) -> int:
    return right - left - count_square(left, right) + 1


if __name__ == '__main__':
    l, r = map(int, input().split())
    print(count_good_number(l, r))
