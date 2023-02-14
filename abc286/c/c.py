# 考察からAを何回かしてからBを行っても良い。
# Aをやる回数全部について調べる
# Bは足りない分行う

n, a, b = map(int, input().split())
s = input()
s += s
ans = 1 << 60 # すごい大きい値を表す
for i in range(n):
    tmp = a * i # Aをやる回数は全部調べる
    for j in range(n // 2):
        # print(s[i + j], s[i + n - 1 - j])
        if s[i + j] != s[i + n - 1 - j]: # 回文になってない部分
            tmp += b
    ans = min(ans, tmp)
print(ans)