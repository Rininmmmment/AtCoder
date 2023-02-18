class unionfind:
	def __init__(self, n):
		self.n = n
		self.par = [ -1 ] * (n + 1)
		self.size = [ 1 ] * (n + 1)
	
	def root(self, x):
		while self.par[x] != -1:
			x = self.par[x]
		return x
	
	def unite(self, u, v):
		rootu = self.root(u)
		rootv = self.root(v)
		if rootu != rootv:
			if self.size[rootu] < self.size[rootv]:
				self.par[rootu] = rootv
				self.size[rootv] += self.size[rootu]
			else:
				self.par[rootv] = rootu
				self.size[rootu] += self.size[rootv]
	
	def same(self, u, v):
		return self.root(u) == self.root(v)

import sys

N, M = map(int, input().split())
G = [ list() for i in range(N+1) ]
U, V = [], []
for i in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
    U.append(u)
    V.append(v)

answer = False
# print(G)
# 条件1：次数が全て2以下か？
for i in range(1, len(G)):
    # print(len(G[i]))
    if len(G[i]) >= 3 or len(G[i]) == 0:
        print("No")
        sys.exit()
# print("条件1通過")

# 条件2：閉路を持っていないか？
uf = unionfind(N)
for i in range(M):
    if uf.same(U[i], V[i]):
        print("No")
        sys.exit()
    uf.unite(U[i], V[i])
print("Yes")