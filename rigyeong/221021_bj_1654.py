# 맞았습니다!!
import sys
k, n = map(int, sys.stdin.readline().split())
line = []
for _ in range(k):
    line.append(int(sys.stdin.readline()))
start, end = 1, max(line)
ans = 0
while start <= end:
    mid = (start + end) //2
    cnt = 0
    for l in line:
        cnt += l // mid
    if cnt < n:
        end = mid -1
    else:
        start = mid +1
        ans=mid
print(ans)