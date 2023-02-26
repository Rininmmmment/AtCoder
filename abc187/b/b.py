n = int(input())
x, y = [None] * n, [None] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        a = (y[i] - y[j]) / (x[i] - x[j])
        if a <= 1 and a >= -1:
            ans += 1
print(ans)