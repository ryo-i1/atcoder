N, M = map(int, input().split())
A = [int(x) for x in input().split()]

X = set(range(1, N + 1)) - set(A)

print(N - M)
print(*X)
