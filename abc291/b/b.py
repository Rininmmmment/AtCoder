N = int(input())
X = list(map(int, input().split()))
X.sort()
validX = X[N:-N]
print(sum(validX) / (3 * N))