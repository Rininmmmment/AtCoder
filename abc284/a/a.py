N = int(input())
S = []
for i in range(N):
    S.append(input())

S.reverse()

for i in range(N):
    print(S[i])