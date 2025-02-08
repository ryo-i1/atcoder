from atcoder.maxflow import MFGraph

vector_dic = {
    (1, 0): 'v',
    (-1, 0): '^',
    (0, 1): '>',
    (0, -1): '<'
}

n, m = map(int, input().split())
S = [list(input()) for _ in range(n)]

graph = MFGraph(n * m + 2)
source = n * m
sink = n * m + 1

for i in range(n):
    for j in range(m):
        if S[i][j] == '#':
            continue

        # odd
        if (i + j) % 2 != 0:
            graph.add_edge(i * m + j, sink, 1)
            continue

        # even
        graph.add_edge(source, i * m + j, 1)

        for ni, nj in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
            if not (0 <= ni < n and 0 <= nj < m):
                continue
            if S[ni][nj] == '#':
                continue

            graph.add_edge(i * m + j, ni * m + nj, 1)

tile_cnt = graph.flow(source, sink)

for edge in graph.edges():
    if edge.flow == 0:
        continue
    if edge.src == source or edge.dst == sink:
        continue

    src_i, src_j = divmod(edge.src, m)
    dst_i, dst_j = divmod(edge.dst, m)

    S[src_i][src_j] = vector_dic[(dst_i - src_i), (dst_j - src_j)]
    S[dst_i][dst_j] = vector_dic[(src_i - dst_i), (src_j - dst_j)]

print(tile_cnt)
for row in S:
    print(*row, sep='')
