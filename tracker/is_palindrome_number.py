def is_palindrome(n):
    rev_n, og_n = 0, n

    while (n):
        last = n % 10
        rev_n = rev_n * 10 + last
        n //= 10

    return "Yes" if og_n == rev_n else "No"


print(is_palindrome(555))
