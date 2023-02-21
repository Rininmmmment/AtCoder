H, W = map(int, input().split())
ans = 0
for i in range(H):
    s = input()
    for j in range(W):
        if s[j] == "#":
            ans += 1

print(ans)