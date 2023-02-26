import sys

N = int(input())
S = input()

position = [0, 0]
positions = set()
for i in range(0, N):
    tpl = tuple(position.copy())
    positions.add(tpl)

    if S[i] == "R":
        position[0] += 1
    if S[i] == "L":
        position[0] -= 1
    if S[i] == "U":
        position[1] += 1
    if S[i] == "D":
        position[1] -= 1

    if tuple(position) in positions:
        print("Yes")
        sys.exit()

print("No")
