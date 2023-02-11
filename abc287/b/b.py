N, M = map(int, input().split())
S, T = [None] * N, [None] * M
for i in range(N):
    S[i] = input()[-3:]
for i in range(M):
    T[i] = input()

Answer = 0
for i in range(N):
    if S[i] in T:
        Answer += 1
print(Answer)