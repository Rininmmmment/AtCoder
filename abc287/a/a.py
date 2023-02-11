N = int(input())
F, A = 0, 0
for i in range(N):
    S = input()
    if S == "For":
        F += 1
    else:
        A += 1

if F > A:
    print("Yes")
else:
    print("No")