n = int(input())
soldiers = list(map(int, input().split()))
soldiers.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(dp)
print(n - max(dp))