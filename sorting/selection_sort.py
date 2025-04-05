a = [6, 4, 3, 8, 9, 1]

n = len(a)
for i in range(n - 1):
    minIndex = i
    for j in range(i + 1, n):
        if a[j] < a[minIndex]:
            minIndex = j
    if minIndex != i:
        a[i], a[minIndex] = a[minIndex], a[i]

print(a)
