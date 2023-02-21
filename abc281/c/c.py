from bisect import bisect_left

N, T = map(int, input().split())
A = list(map(int, input().split()))
sumA = sum(A)
cumulative_sums = [None] * (N + 1)

# [i]はA[i-1]までの累積和
cumulative_sums[0] = 0
for i in range(1, N+1):
    cumulative_sums[i] = cumulative_sums[i-1] + A[i-1]

time = T % sumA
ans = bisect_left(cumulative_sums, time)
count = time - cumulative_sums[ans-1]
print(ans, count)


# print(cumulative_sums)
# print(time)