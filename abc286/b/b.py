N = int(input())
S = input()
while True:
    fin = 1
    for i in range(N-1):
        if S[i] == "n" and S[i+1] == "a":
            S = S[:i+1] + "y" + S[i+1:]
            fin = 0
            break
    if fin:
        break
print(S)