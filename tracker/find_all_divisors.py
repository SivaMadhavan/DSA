from math import sqrt


def printDivisors(n):
    result = [1]
    end = sqrt(n)
    for a in range(2, int(end) + 1):
        if n % a == 0:
            result.append(a)
            result.append(int(n / a))
    result.append(n)

    return sorted(list(set(result)))



print(printDivisors(361))
