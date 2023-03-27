from Europe import *

def test(A, orient_A):
    not_visited = [i for i in range(1, len(A))]
    x = 0
    d = [0]
    rod = [0 for i in range(len(A))]

    for i in range(len(A) - 1):
        d.append(float('inf'))

    while len(not_visited) != 0:
        mn = float('inf')
        for i in not_visited:
            if A[x][i] + d[x] < d[i]:
                rod[i] = x
                d[i] = A[x][i] + d[x]

            if d[i] < mn:
                mn = d[i]
                key_mn = i

        orient_A[rod[key_mn]][key_mn] = A[rod[key_mn]][key_mn]
        not_visited.remove(key_mn)
        x = key_mn

    return d, orient_A

print(test(distance, orient_Europe))

