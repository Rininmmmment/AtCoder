# hige in listはクソ遅い。setにすると速くなる！

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = set(list(map(int,input().split())))
X = int(input())

dp = [None] * (X+1) # i段目に登れればTrue
dp[0] = True

for i in range(1, X+1):
    for j in range(N):
        if i in B:
            continue
        elif i >= A[j]:
            if dp[i-A[j]]:
                dp[i] = True

if dp[X]:
    print("Yes")
else:
    print("No")