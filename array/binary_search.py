def binary_search(arr, k):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if k == arr[mid]:
            return mid
        elif k < array[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


array = sorted(list(set(list(map(int, input("enter Elements").split(","))))))
key = int(input("Enter an element you want to search : "))
print("The element found at index : ", binary_search(array, key))
