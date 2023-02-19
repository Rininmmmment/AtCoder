def solve(n, s):
    # 含まれる1の個数
    k = s.count("1")

    # 1が奇数個の時は不可能
    if k % 2 == 1:
        return -1
    adj = s.count("11")

    # 1が4個以上、1が0個、11が0個のどれかを満たす場合はk//2回で可能
    if k >= 4 or k == 0 or not adj:
        return k // 2

    # 011 110 の時は不可能
    if n == 3:
        return -1
    
    # 0110 のときは3回で可能
    if s == "0110":
        return 3
    return 2


# Driver Code
if __name__ == '__main__':
    
    T = int(input())
    for t in range(T):
        N = int(input())
        S = input()
        print(solve(N, S))