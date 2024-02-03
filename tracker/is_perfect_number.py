from math import sqrt, ceil


def is_perfect(n):
    _sum = 1
    end = sqrt(n)
    for a in range(2, int(end) + 1):
        if n % a == 0 and a != n/a:
            _sum += a + n/a
    return int(_sum == n)


print(is_perfect(6))
