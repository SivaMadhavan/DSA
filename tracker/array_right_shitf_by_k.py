def array_rotate_by_one(arr, k, n):
    k = k % n
    l, r = 0, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1

    l, r = 0, k - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l+1, r-1

    l, r = k, len(arr) - 1
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l, r = l + 1, r - 1


print(array_rotate_by_one([1, 2, 3, 4, 5], 2, 5))
