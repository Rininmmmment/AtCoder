N = int(input())
S = list(input())


for i in range(1, N):
    answer = 0
    for j in range(N-i):
        # print(S[j], S[i+j])
        if S[j] != S[j+i]:
            answer += 1
        else:
            break
    print(answer)