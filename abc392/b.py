N, M = map(int, input().split())
A = [int(x) for x in input().split()]

X = [i for i in range(1, N + 1) if i not in A]

print(N - M)
print(*X)
