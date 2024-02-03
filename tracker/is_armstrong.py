def armstrongNumber(n):
    result, og_number = 0, n

    while (n):
        last_digit = n % 10
        if last_digit:
            result += last_digit * last_digit * last_digit
        n //= 10
    return 1 if og_number == result else 0


print(armstrongNumber(371))
