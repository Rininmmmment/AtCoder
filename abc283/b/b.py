def solve(n, a, query):
    k = query[1]
    if query[0] == 2:
        print(A[k-1])

    else:
        x = query[2]
        A[k-1] = x


if __name__ == '__main__':
    
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for q in range(Q):
        query = list(map(int, input().split()))
        solve(N, A, query)