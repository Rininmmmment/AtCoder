import string

S = list(input())
S.reverse()
# print(S)

alphabets = [""] + list(string.ascii_uppercase)

answer = 0
for i in range(len(S)):
    answer += (26 ** i) * alphabets.index(S[i])

print(answer)