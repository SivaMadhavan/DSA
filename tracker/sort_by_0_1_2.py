def sort012(arr):
    # code here
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in arr:
        if i == 0:
            count_0 += 1
        if i == 1:
            count_1 += 1
        if i == 2:
            count_2 += 1

    for i in range(count_0):
        arr[i] = 0

    for i in range(count_0, count_0 + count_1):
        arr[i] = 1

    for i in range(count_0 + count_1, count_0 + count_1 + count_2):
        arr[i] = 2


arr = [0, 2, 1, 2, 0]
sort012([0, 2, 1, 2, 0])
print(arr)
