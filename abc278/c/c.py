import collections

N, Q = map(int, input().split())
T, A, B = [None] * Q, [None] * Q, [None] * Q
for i in range(Q):
    T[i], A[i], B[i] = map(int, input().split())

G = collections.defaultdict(set)
for i in range(Q):
    if T[i] == 1:
        G[A[i]].add(B[i])

    if T[i] == 2:
        if B[i] in G[A[i]]:
            G[A[i]].remove(B[i])

    if T[i] == 3:
        if A[i] in G[B[i]] and B[i] in G[A[i]]:
            print("Yes")
        else:
            print("No")