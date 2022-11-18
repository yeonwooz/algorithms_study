# 백준 17271
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [1]*(n+1) # DP전체를 1로 

if n>=m: # 전제조건
    dp[m] = 2 # m일 때는 a랑 b -> 2
for i in range(m+1, n+1): # n-1초는 채웠으니 +1, n-m초는 채웠으니 +m
    dp[i] = (dp[i-1]+dp[i-m])%1000000007

print(dp[n]%1000000007)

