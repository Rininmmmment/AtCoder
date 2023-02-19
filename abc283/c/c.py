S = input()

btnPushCount = 0
btnPushCount += S.count("00")
S = S.replace("00", "")


btnPushCount += len(S)

print(btnPushCount)