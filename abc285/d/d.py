from collections import deque, defaultdict

# 入力
M = int(input())
S, T = [None] * M, [None] * M
for i in range(M):
    S[i], T[i] = input().split()

# 文字列を数値に変換
li = set(S + T)
N = len(li)
henkan = defaultdict(int)
count = 0
for item in li:
    henkan[item] = count
    count += 1

G = [[] for _ in range(N)]
deg = [0 for _ in range(N)]
for i in range(M):
    G[henkan[T[i]]].append(henkan[S[i]])
    deg[henkan[S[i]]] += 1

def isCycle(N, G, deg):

    """
    N: 頂点の数
    M: 辺の数
    G: グラフ(終点のインデックスから、始点の番号を取り出す)
    deg: 頂点 v の出次数
    """

    # 問題文の指示より、隣接リストの中身をソートしておく
    for i in range(N):
        G[i].sort()

    que = deque([]) # 探索候補の頂点番号を入れるキュー
    # 頂点 v = 0, 1, …, N-1 の順に
    for v in range(N):
        # 頂点 v の出次数が最初の時点で 0 ならば、キューに v を入れる
        if deg[v] == 0: que.append(v)

    order = []  # トポロジカルソート順を格納するための配列

    # キューに要素が残っている限り
    while len(que) > 0:
        # キューの先頭要素 v を取り出し、配列 order に挿入する
        v = que.popleft()
        order.append(v)
        
        # 頂点 v に隣接している頂点 v2 について、
        for v2 in G[v]:
            # v2 の出次数を 1 減らして、もし出次数が 0 になったらキューに v2 を入れる
            deg[v2] -= 1
            if deg[v2] == 0: que.append(v2)

    # 全ての頂点が order に含まれているかによって、答えを変える
    if len(order) != N:
        # order の要素数が N でなければ、order に含まれていない頂点があるので Yes
        return True
    else:
        # order の要素数が N であれば、すべての頂点が order に含まれているので No
        return False

if not isCycle(N, G, deg):
    print("Yes")
else:
    print("No")