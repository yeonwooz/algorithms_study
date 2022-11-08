# 1337 올바른 배열
import sys
input = sys.stdin.readline

N = int(input())
arr = [ int(input()) for _ in range (N) ]
result = 5

for i in range(N):
    cnt = 0
    for j in range(arr[i], arr[i]+5):
        if j not in arr:
            cnt+=1
    result = min(result, cnt)

print(result)