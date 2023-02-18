def match_or_not(a, b):
    if a == "?" or b == "?" or a == b:
        return True
    else:
        return False

S = list(input())
T = list(input())

isMatchFromFront = [False] * (len(T)+1)
isMatchFromEnd = [False] * (len(T)+1)

# 前から0, 1, 2, ...番目まではマッチするか？（累積和のような感じ）
isMatchFromFront[0] = True
for i in range(len(T)):
    if not match_or_not(S[i], T[i]):
        break
    else:
        isMatchFromFront[i+1] = True



# 後ろから0, 1, 2, ...番目まではマッチするか？（累積和のような感じ）
# SやT自体を逆順にすることで、前から考えた時と同じコードで書けるようにしている
S.reverse()
T.reverse()

isMatchFromEnd[0] = True
for i in range(len(T)):
    if not match_or_not(S[i], T[i]):
        break
    else:
        isMatchFromEnd[i+1] = True

# 出力
for x in range(len(T)+1):
    if isMatchFromFront[x] and isMatchFromEnd[len(T)-x]:
        print("Yes")
    else:
        print("No")
        
# print(isMatchFromFront)
# print(isMatchFromEnd)