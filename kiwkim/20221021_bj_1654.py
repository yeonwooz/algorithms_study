#랜선 자르기 김기운
#https://www.acmicpc.net/problem/1654
import sys
readl = sys.stdin.readline

K, N = map(int, readl().split())
ropes = []

for i in range(K):
    ropes.append(int(readl()))
start = 1
end = max(ropes)

while start <= end:
    mid = (start + end) // 2
    curnum = 0
    for rope in ropes:
        curnum += rope//mid
    if curnum < N:
        end = mid - 1
    else:
        start = mid + 1
        result = mid
print(result)