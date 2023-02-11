N, M = map(int, input().split())
G = [ list() for i in range(N+1) ]
for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

print(G)