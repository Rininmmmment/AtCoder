N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
Q = int(input())
l, r = [None] * Q, [None] * Q
for i in range(Q):
    l[i], r[i] = map(int, input().split())

# S[i] = mod K が i になる要素の和
S = [[0]*(K-1) for i in range()]

for i in range(Q):
    for j in range(l[i], r[i]+1):
        S[j % K] += A[j]
    if S.count(S[0]) == len(S):
        print("Yes")
    else:
        print("No")
    S = [0] * K