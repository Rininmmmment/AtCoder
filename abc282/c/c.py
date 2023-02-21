N = int(input())
S = list(input())

height = 0
for i in range(N):
    if S[i] == '"' and height == 0:
        height = 1
    elif S[i] == '"' and height == 1:
        height = 0

    if S[i] == ',' and height == 0:
        S[i] = '.'

for s in S:
    print(s, end="")
print()
