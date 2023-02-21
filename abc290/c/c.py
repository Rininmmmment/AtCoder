N, K = map(int, input().split())
A = list(map(int, input().split()))
A = list(set(A))
A.sort()

B = set(A[:K])
ans = 0
for i in range(K):
    if i in B:
        ans = i + 1
    else:
        break
print(ans)