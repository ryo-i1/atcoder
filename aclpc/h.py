from atcoder.twosat import TwoSAT

N, D = map(int, input().split())
flags = [tuple(map(int, input().split())) for _ in range(N)]

twosat = TwoSAT(N)

for i in range(N - 1):
    for j in range(i + 1, N):
        if abs(flags[i][0] - flags[j][0]) < D:
            twosat.add_clause(i, False, j, False)
        if abs(flags[i][0] - flags[j][1]) < D:
            twosat.add_clause(i, False, j, True)
        if abs(flags[i][1] - flags[j][0]) < D:
            twosat.add_clause(i, True, j, False)
        if abs(flags[i][1] - flags[j][1]) < D:
            twosat.add_clause(i, True, j, True)

if twosat.satisfiable():
    print('Yes')
    ans = twosat.answer()
    for i in range(N):
        if ans[i]:
            print(flags[i][0])
        else:
            print(flags[i][1])
else:
    print('No')
