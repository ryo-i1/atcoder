max_a, max_b, max_c, x = [int(input()) for _ in range(4)]

best_a = min(max_a, x // 500)

ans = 0
for a in range(best_a, -1, -1):
    res_x = x - 500 * a

    best_b = min(max_b, res_x // 100)
    res_x -= 100 * best_b

    best_c = min(max_c, res_x // 50)
    res_c = max_c - best_c
    res_x -= 50 * best_c
    if res_x > 0:
        break

    n = min(best_b, res_c // 2) + 1
    ans += n

print(ans)
