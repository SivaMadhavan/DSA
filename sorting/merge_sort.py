arr = [6, 6, 3, 8, 9, 1]
n = len(arr)


def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)


def merge(arr, l, mid, r):
    larr = arr[l:mid + 1]
    rarr = arr[mid + 1:r + 1]

    i = j = 0
    k = l

    while i < len(larr) and j < len(rarr):
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1
        k += 1

    while i < len(larr):
        arr[k] = larr[i]
        i += 1
        k += 1

    while j < len(rarr):
        arr[k] = rarr[j]
        j += 1
        k += 1


merge_sort(arr, 0, n - 1)
print(arr)
