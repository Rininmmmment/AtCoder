from collections import defaultdict
S = input()

# 次括弧が閉じたら取り出すアルファベットの小文字。中断したものリスト。
nextItems = []

# 箱の中身
boxContents = defaultdict(int)

# 今見ている () の中身を管理
currentSet = set()



"""
処理の説明：
文字列Sについて、1文字目から順番に見ていく。
今見ている文字をsとする。
中断とは、まだ閉じていなくて取り出していない括弧の中身のこと。

1. sが "(" のとき、
   新しい括弧が始まるので、まだ閉じてないものは中断する。
   currentSetの中身をリセットする。

2. sが ")" のとき、
   箱からボールを取り出す（currentSet）。
   中断していた括弧の分をcurrentSetに入れる。

3. sが アルファベット のとき、
   a 箱の中にすでにあれば終了。
   b なければ箱の中に入れる。
     currentSetに入れて今見ている括弧の中に存在することを管理。

"""

for s in S:
    # 新しい () の登場にあわせて、今見ている () を X に格納 
    if s=="(":
        nextItems.append(currentSet)
        currentSet = set()
        continue

    if s==")":
        # 箱からボールを取り出す
        for t in currentSet:
            boxContents[t] = 0

        # 直前の () を取り出す
        currentSet = nextItems.pop()
        continue

    
    # 被りを検出したら気を失い終了
    if boxContents[s] != 0:
        print("No")
        exit()
    
    # s を使用済みに変更
    boxContents[s] = 1
    # 今見ている () に s が存在することを記録
    currentSet.add(s)

print("Yes")