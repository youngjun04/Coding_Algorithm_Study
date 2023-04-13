n = int(input())
ti = []
pi = []

for _ in range(n):
    t, p = map(int, input().split())
    ti.append(t)
    pi.append(p)

dp = [0] * (n + 1)
max_value = 0

for i in range(n - 1, -1, -1):
    time = ti[i] + i
    if time <= n:
        dp[i] = max(pi[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)