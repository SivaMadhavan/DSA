def thirdLargest(a, n):
    first = second = third = a[0]
    for i in a:
        if i > first:
            first = i
            if first > second:
                second = first
                if second > third:
                    third = second
    return first, second, third


print(thirdLargest([2, 4, 1, 3, 5], 5))
