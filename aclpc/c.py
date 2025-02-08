from atcoder.math import floor_sum

t = int(input())

for _ in range(t):
    n, m, a, b = map(int, input().split())

    print(floor_sum(n, m, a, b))
