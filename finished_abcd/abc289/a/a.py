s = input()
ans = []
for i in range(len(s)):
    if s[i] == "0":
        ans.append("1")
    if s[i] == "1":
        ans.append("0")
for i in ans:
    print(i, end="")
print("")