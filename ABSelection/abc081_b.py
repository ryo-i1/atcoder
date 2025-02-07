N = int(input())
A = [int(a) for a in input().split()]

n = 0
is_end = False
while True:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] /= 2
        else:
            is_end = True
            break

    if is_end:
        break
    else:
        n += 1

print(n)
