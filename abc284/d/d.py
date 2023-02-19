import math

def make_divisors(n):
    p, q = 0, 0
    for i in range(2, int(n**(1/3))+1):
        if n % i == 0:
            if n % (i ** 2) == 0:
                p = i
                q = n // (i ** 2)
            else:
                q = i
                p = int((n // i) ** 0.5)
            break

    return [p, q]



# Driver Code
if __name__ == '__main__':
    
    T = int(input())
    for t in range(T):
        N = int(input())
        print(*make_divisors(N))
