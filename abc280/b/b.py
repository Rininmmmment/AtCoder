N = int(input())
S = list(map(int, input().split()))

A = [None] * N
A[0] = S[0]
B = [0] * N
B[0] = A[0]  # B[i]はA[i-1]までの累積和
for i in range(1, N):
    A[i] = S[i] - B[i-1]
    B[i] = B[i-1] + A[i]
print(*A)
