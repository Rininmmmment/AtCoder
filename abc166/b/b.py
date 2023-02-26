from collections import defaultdict

n, k = map(int, input().split())
sunuke = [False] * n

for i in range(k):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        sunuke[a - 1] = True
    
ans = 0
for i in range(n):
    if not sunuke[i]:
        ans += 1

print(ans)