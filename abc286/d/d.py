N, X = map(int, input().split())
A, B = [None] * N, [None] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

C = []
for i in range(N):
    for j in range(B[i]):
        C.append(A[i])

# i枚の効果で和をjにできるか
dp = [[None] * (X + 1) for i in range(len(C)+1)]
dp[0][0] = True
for j in range(1, X+1): # 0枚の時は全てFalse
	dp[0][j] = False

for i in range(1, len(C)+1):
	for j in range(0,X+1):
		if j < C[i-1]:
            # カードiなしですでに和がjならTrue
			if dp[i-1][j] == True:
				dp[i][j] = True
            # そうでなければA[i-1]を足してもjにならないのでFalse
			else:
				dp[i][j] = False

		if j >= C[i-1]:
            # すでに和がj、もしくはカードi-1までで和がj-A[i-1]ならTrue
			if dp[i-1][j] == True or dp[i-1][j-C[i-1]] == True:
				dp[i][j] = True
			else:
				dp[i][j] = False
# 出力
ans = False
for i in range(N):
    if dp[i][X] == True:
        ans = True

if dp[N][X]:
	print("Yes")
else:
	print("No")