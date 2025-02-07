N, Y = map(int, input().split())

z = Y // 1000
res_N = z - N

x = (res_N // 36) * 4
z -= x * 10
res_N = res_N % 36

add_x = res_N % 4
x += add_x
z -= add_x * 10
res_N -= add_x * 9

add_y = res_N // 4
y = add_y
z -= add_y * 5
res_N -= add_y * 4

if y < 0:
    n = ((-y - 1) // 9) + 1
    x -= 4 * n
    y += 9 * n
    z -= 5 * n

if x >= 0 and z >= 0:
    print(x, y, z)
else:
    print(-1, -1, -1)
