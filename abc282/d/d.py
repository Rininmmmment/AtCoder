import sys
from collections import defaultdict
sys.setrecursionlimit(120000)

# pos は現在位置、visited[x] は頂点 x が青色かどうかを表す真偽値
def dfs(pos, G, visited, color):
	visited[pos] = True
	color[pos] = 0
	for i in G[pos]:
		if visited[i] == False:
			dfs(i, G, visited)

N, M = map(int, input().split())
G = defaultdict(list)
u, v = [None] * M, [None] * M
for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)


visited = [ False ] * (N + 1)
color = [ None ] * (N + 1)

dfs(1, G, visited)

answer = True
for i in range(1, N + 1):
	if visited[i] == False:
		answer = False
print(answer)
print(G)