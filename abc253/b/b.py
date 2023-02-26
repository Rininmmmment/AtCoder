h, w = map(int, input().split())
position = []
for i in range(h):
    str = input()
    for j in range(w):
        if str[j] == "o":
            position.append([i, j])

ans = abs(position[0][0] - position[1][0]) + abs(position[0][1] - position[1][1])
print(ans)