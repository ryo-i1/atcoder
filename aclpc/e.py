from atcoder.mincostflow import MCFGraph

B = 1 << 50

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

graph = MCFGraph(N * 2 + 2)
start, goal = N * 2, N * 2 + 1

edges = [[-1] * N for _ in range(N)]
for i in range(N):
    graph.add_edge(start, i, K, 0)
    graph.add_edge(i + N, goal, K, 0)

    for j in range(N):
        edges[i][j] = graph.add_edge(i, j + N, 1, B - A[i][j])

graph.add_edge(start, goal, N * K, B)

_, cost = graph.flow(start, goal, N * K)
print(B * N * K - cost)

ans_grid = [['.'] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph.get_edge(edges[i][j]).flow > 0:
            ans_grid[i][j] = 'X'

for row in ans_grid:
    print(*row, sep='')
