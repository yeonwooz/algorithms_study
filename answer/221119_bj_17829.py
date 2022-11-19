#222-풀링 홍리경
#https://www.acmicpc.net/problem/17829

import sys
N,M = map(int, sys.stdin.readline().split())
dp =  [1] * (N+1)
if N >= M:
    dp[M] = 2
for i in range(M+1, N+1):
    dp[i] = (dp[i-1] + dp[i-M]) % 1000000007
print(dp[N]%1000000007)