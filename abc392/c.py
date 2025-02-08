N = int(input())
P = [int(x) for x in input().split()]
Q = [int(x) for x in input().split()]

data = []
for i in range(len(P)):
    data.append((Q[i], P[i]))
data_sorted = sorted(data)

S = []
for i in range(len(data)):
    q, p = data_sorted[i]

    s, _ = data[p - 1]
    S.append(s)

print(*S)
