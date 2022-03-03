def count_K_number(n: int, k: int) -> int:
    if n == 1:
        return k - 1
    if n == 2:
        return (k - 1) * k
    digits = (k - 1) * k
    zero = k - 1
    for _ in range(3, n + 1):
        digits, zero = (digits + zero) * (k - 1), digits
    return digits


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(count_K_number(n, k))
