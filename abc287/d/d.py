S = input()
T = input()
isMatchFromFront = [None] * len(T)
isMatchFromEnd = [None] * len(T)

for i in range(len(T)):
    if not(S[i] == "?" or T[i] == "?"):
        isMatchFromFront[i] = False
    else:
        isMatchFromFront[i] = True

for i in reversed(range(len(T))):
    if not(S[i] == "?" or T[i] == "?"):
        isMatchFromEnd[i] = False
    else:
        isMatchFromEnd[i] = True

print(isMatchFromFront)
print(isMatchFromEnd)

for x in range(len(T)+1):
    ans = True
    if isMatchFromFront[x]:
        




    for i in range(len(T)):
        if Sx[i] == "?" or T[i] == "?":
            pass
        else:
            if Sx[i] != T[i]:
                ans = False
        # print(Sx[i], T[i], ans)
    if ans:
        print("Yes")
    else:
        print("No")
