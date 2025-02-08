import numpy as np


N = int(input())

data = []
for _ in range(N):
    line = [int(x) for x in input().split()]

    k = line[0]
    A = line[1:]

    prod = np.bincount(A) / k

    data.append(prod)

best = -1
for i in range(N):
    for j in range(i + 1, N):
        l = min(len(data[i]), len(data[j]))

        prod = np.sum(data[i][:l] * data[j][:l])
        if prod > best:
            best = prod

print(best)
