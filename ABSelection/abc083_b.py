N, A, B = map(int, input().split())

ans = 0
for i in range(N + 1):
    digits = [int(d) for d in str(i)]
    if not A <= sum(digits) <= B:
        continue
    ans += i

print(ans)
