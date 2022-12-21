# 11653 소인수분해
import sys, math
input = sys.stdin.readline

N = int(input())


for i in range(2, N+1):
    while (N % i == 0):
        N = N / i
        print(i)

