S = input()

answer = 0
for s in S:
    if s == "v":
        answer += 1
    if s == "w":
        answer += 2

print(answer)
