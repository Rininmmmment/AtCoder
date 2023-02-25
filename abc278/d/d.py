import collections

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
difference = collections.defaultdict(int)
flg = True

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        difference = collections.defaultdict(int)
        x = query[1]
        flg = False

    if query[0] == 2:
        difference[query[1]-1] += query[2]
    
    if query[0] == 3:
        if flg:
            print(A[query[1]-1] + difference[query[1]-1])
        else:
            print(x + difference[query[1]-1])