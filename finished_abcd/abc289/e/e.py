from collections import deque

t = int(input())
for i in range(t):
    N, M = map(int,input().split())
    C = list(map(int,input().split()))
    G = [[] for i in range(N+1)]
    for i in range(M):
        x, y = map(int,input().split())
        G[x].append(y)
        G[y].append(x)

    s = [[10**6]*(N+1) for i in range(N+1)]

    Q = deque()
    Q.append((1,N))

    s[1][N] = 0

    while Q:
        x,y = d.popleft()
        if x ==n and y==1:
            break
        if s[n][1] <= s[x][y]:
            break
        for i in rin[x]:
            for j in rin[y]:
                if c[i-1] == c[j-1]:
                    continue
                if s[i][j] == 10**6:
                    d.append((i,j))
                    s[i][j] = s[x][y] + 1
                    if i == n and j == 1:
                        break
                    
    print(s[n][1] if s[n][1] != 10**6 else -1)