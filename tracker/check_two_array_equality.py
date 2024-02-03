def check_equality(A, B):
    A.sort()
    B.sort()
    return (int(A == B))


A = [20, 6, 17, 15, 19]
B = [6, 17, 20, 19, 19]
print(check_equality(A, B))
