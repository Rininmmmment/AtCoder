def Enumerate(A):
	SumList = []
	for i in range(2 ** len(A)):
		li = []
		for j in range(len(A)):
			wari = (2 ** j)
			if (i // wari) % 2 == 1:
				li = li + A[j]
		SumList.append(li)
	return SumList

N, M = map(int, input().split())
C, S = [None] * M, [None] * M
for i in range(M):
    C[i] = int(input())
    S[i] = list(map(int, input().split()))

s = Enumerate(S)
Answer = 0
cnt = [False] * N
for s_item in s:
    for i in range(1, N+1):
        if i in s_item:
            cnt[i-1] = True
    if not False in cnt:
        Answer += 1
    cnt = [False] * N
print(Answer)

