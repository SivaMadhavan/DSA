arr = [45, 23, 89, 12, 67, 3, 90, 34, 11, 76]


def find_pivot(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quicks_sort(arr, low, high):
    if low < high:
        pivot_index = find_pivot(arr, low, high)
        quicks_sort(arr, low, pivot_index - 1)
        quicks_sort(arr, pivot_index + 1, high)


quicks_sort(arr, 0, len(arr) - 1)
print(arr)
