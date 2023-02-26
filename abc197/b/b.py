H, W, X, Y = map(int, input().split())
X -= 1  # 0スタートにしたいので、-1します
Y -= 1  # Xは縦方向で、Yは横方向です。
grid = []

for _ in range(H):
    s = input()
    grid.append(s)

ans = 1  # (X, Y)自身も含むので、初期値は1にします
         # なお、四方向ごとに(X, Y)自身も含める実装の場合、1-4=-3が初期値になります

# 上　X-1 ～ 0
for row in reversed(range(X)):
    if grid[row][Y] == "#":
        # この先は見えないのでbreakします
        break
    else:
        ans += 1

# 下 X+1 ～ H-1
for row in range(X + 1, H):
    if grid[row][Y] == "#":
        break
    else:
        ans += 1

# 左 Y-1 ～ 0
for col in reversed(range(Y)):
    if grid[X][col] == "#":
        break
    else:
        ans += 1

# 右 Y+1 ～ W-1
for col in range(Y + 1, W):
    if grid[X][col] == "#":
        break
    else:
        ans += 1

print(ans)