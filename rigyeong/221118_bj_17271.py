#맞았습니다!
import sys
n, m = map(int, sys.stdin.readline().split())
if m > n: print(1)
elif m == n: print(2)
else:
    dp = [0] * (n+1)
    for i in range(1,m+1):
        if i == m: dp[i] = 2
        else: dp[i] = 1
    for i in range(m+1, n+1):
        dp[i] = (dp[i-m] + dp[i-1]) % 1000000007
    print(dp[i])
    
'''
import sys
n, m = map(int, sys.stdin.readline().split())
dp = [0] * max(m, n+1)
dp[:m] = [1] * m
for i in range(m, n+1):
    dp[i] = (dp[i-m] + dp[i-1]) % 1000000007
print(dp[n])
'''