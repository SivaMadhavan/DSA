def left_shift_by_k(arr: list, k: int) -> list:
    n = len(arr)
    k = k % n
    l, r = 0, n - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1

    l, r = n - k, n - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1

    l, r = 0, n - k - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1

    return arr


print(left_shift_by_k([1, 2], 1))
