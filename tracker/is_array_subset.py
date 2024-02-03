Arr1 = [1, 2, 3, 4, 5, 1, 1, 1]
Arr2 = [1,2,3,1]

hash_map = {}
for i in Arr2:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1

for i in Arr1:
    if i in hash_map:
        hash_map[i] -= 1

for i in hash_map.values():
    if i >= 0:
        print("Not a subset")

print("Subset")