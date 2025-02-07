N = int(input())

failed = False
pt, px, py = 0, 0, 0
for i in range(N):
    t, x, y = map(int, input().split())

    d = abs(x - px) + abs(y - py)
    d -= t - pt

    if d > 0 or -d % 2 == 1:
        failed = True
        break

    pt, px, py = t, x, y

for _ in range(i + 1, N):
    input()

if failed:
    print('No')
else:
    print('Yes')
