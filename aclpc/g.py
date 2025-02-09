from atcoder.scc import SCCGraph

N, M = map(int, input().split())

graph = SCCGraph(N)
for _ in range(M):
    a, b = map(int, input().split())
    graph.add_edge(a, b)

groups = graph.scc()

print(len(groups))
for group in groups:
    print(len(group), *group)
