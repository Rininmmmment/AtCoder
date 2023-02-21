N = int(input())
A = list(map(int, input().split()))

def isPalindrome(s):
    return s == s[::-1]

print(isPalindrome(A))