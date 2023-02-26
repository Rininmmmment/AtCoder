from sys import exit

N = int(input())
moji1 = {"H", "D", "C", "S"}
moji2 = {"A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"}
li = []

for i in range(N):
    S = list(input())
    if not S in li and S[0] in moji1 and S[1] in moji2:
        li.append(S)
        continue
    else:
        print("No")
        exit()
print("Yes")
