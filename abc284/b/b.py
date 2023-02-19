def solve(n, a):
    oddCount = 0
    for i in range(n):
        if a[i] % 2 == 1:
            oddCount += 1
    return oddCount


# Driver Code
if __name__ == '__main__':
    
    T = int(input())
    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        print(solve(N, A))