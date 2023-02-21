import sys
S = input()

if S[0].isupper() and S[-1].isupper():
    if S[1:-1].isdecimal() and S[1] != "0":
        if 100000 <= int(S[1:-1]) and int(S[1:-1]) <= 999999:
            print("Yes")
            sys.exit()

print("No")
