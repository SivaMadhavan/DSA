arr = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
m = len(arr)
n = len(arr[0])
maxSum = 0
for a in range(m-2):
    for b in range(n - 2):
        curSum = 0
        for i in range(a, a+3):
            for j in range(b, b+3):
                if not (i==a+1 and (j-b)%2==0):
                    print(arr[i][j], end=' ')
                    curSum += arr[i][j]
            print("\n")
        maxSum = max(curSum, maxSum)
print(maxSum)
