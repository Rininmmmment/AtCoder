N, M = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

answer = 0
for i in range(N-1):
    for j in range(i+1, N):
        dd = True
        for k in range(M):
            if S[i][k] == "x" and S[j][k] == "x":
                dd = False
        if dd:
            answer += 1
    

print(answer)