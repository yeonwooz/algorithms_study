import sys
N, M = map(int, sys.stdin.readline().split())

dp = [0] * max(M,N+1)
dp[:M] = [1] * M

for i in range(M, N+1):
    dp[i] = (dp[i-1] + dp[i-M]) % 1000000007

print(dp[N])