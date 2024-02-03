from math import sqrt


def isPrime(N):
    for i in range(2, int(sqrt(N)) + 1):
        if not N % i:
            return 0
    return 1


print(isPrime(545))
