# 맞았습니다!
import sys
from heapq import heappop, heappush
n = int(sys.stdin.readline())
h = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x:
        heappush(h, (abs(x), x))
    else:
        if h: 
            p = heappop(h)
            print(p[1])
        else: 
            print(0)