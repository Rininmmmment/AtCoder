N, A, B = map(int, input().split())
S = input()

def sousaA(S):
    S = S[1:] + S[0]
    return S

def sousaB(S, i, x):
    return S[:i-1] + x + S[i:]
    
