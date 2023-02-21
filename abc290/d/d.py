def solve1(N, D):
    answers = [None] * N
    for i in range(N):
    # 何回めに印をつけられるか
        answers[i] = (i % D) * ((N - 1) // D + 1) + (i // D)
    return answers

if __name__ == '__main__':
    
    T = int(input())
    for t in range(T):
        N, D, K = map(int, input().split())
        if N >= D:
            list = solve1(N, D)
            print(list.index(K-1))
        else:
            D = D % N
            list = solve1(N, D)
            print(list.index(K-1))