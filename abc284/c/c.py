from collections import defaultdict
import sys
sys.setrecursionlimit(120000)

def dfs(pos, G, visited):
	visited[pos] = True
	for i in G[pos]:
		if visited[i] == False:
			dfs(i, G, visited)

N, M = map(int, input().split())
G = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [ False ] * (N + 1)
visited[0] = True

connectedComp = 0
while False in visited:
    falseIndex = visited.index(False)
    dfs(falseIndex, G, visited)
    connectedComp += 1
    # print(connectedComp)
    # print(visited)
    # print("---------------")

print(connectedComp)
