a, b = map(int, input().split())

G = [[] for _ in range(15)]
for i in range(7):
    G[i].append((i+1) * 2)
    G[i].append((i+1) * 2 + 1)

if b in G[a-1]:
    print("Yes")
else:
    print("No")