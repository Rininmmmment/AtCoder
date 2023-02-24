A, B = map(int, input().split())

def func(n):
    return B * n + A / ((n + 1) ** 0.5)

def func_d():
    a = (2 * B / A) ** (-2 / 3) - 1
    if a < 0:
        return 0
    return int(a)
a = []
for i in range(-1, 2):
    if func_d() + i + 1 == 0:
        continue
    else:
        a.append(func(func_d() + i))
print(min(a))