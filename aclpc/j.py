from atcoder.segtree import SegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))

st = SegTree(max, -1, A)

for _ in range(Q):
    t, x, y = map(int, input().split())

    if t == 1:
        st.set(x - 1, y)
    elif t == 2:
        print(st.prod(x - 1, y))
    elif t == 3:
        print(st.max_right(x - 1, lambda p: p < y) + 1)
