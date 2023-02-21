N, K = map(int, input().split())
S = input()

yosen = []
for i in range(N):
    if S[i] == "o":
        yosen.append(i)
yosen = yosen[:K]

ans = ["x"] * N
for i in range(K):
    ans[yosen[i]] = "o"

for i in range(N):
    print(ans[i], end="")
print()