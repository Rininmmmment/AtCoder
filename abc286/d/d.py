N, X = map(int, input().split())
A, B = [], []
for i in range(N):
    ai, bi = map(int, input().split())
    A.append(ai)
    B.append(bi)
    
dp = [[False for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0] = True
for j in range(1, X+1):
    dp[0][j] = False

for i in range(1, N + 1):
    for j in range(X + 1):
        if dp[i-1][j]:
            dp[i][j] = True
        for k in range(1, B[i-1]+1):
            index = j-k*A[i-1]
            if 0 <= index:
                if dp[i-1][index] == True:
                    dp[i][j] = True

if dp[N][X]:
    print("Yes")
else:
    print("No")