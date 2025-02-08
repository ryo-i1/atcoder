from atcoder.fenwicktree import FenwickTree

n, q = map(int, input().split())
a = [int(x) for x in input().split()]

ft = FenwickTree(n)
for i, el in enumerate(a):
    ft.add(i, el)

for _ in range(q):
    t, l, r = map(int, input().split())

    if t == 0:
        ft.add(l, r)
    elif t == 1:
        print(ft.sum(l, r))
