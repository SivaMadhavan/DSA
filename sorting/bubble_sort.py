a = [6, 4, 3, 8, 9, 1]

n = len(a)
for i in range(n):
    swapped = False
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
    if not swapped:
        break
print(a)
