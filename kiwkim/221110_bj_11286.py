#11286 절댓값 힙

import sys
import heapq
readl = sys.stdin.readline

n = int(readl())
heap_minus = []
heap_plus = []
cnt = 0
for i in range(n):
    put = int(readl())
    if put > 0:
        heapq.heappush(heap_plus, put);
    elif put < 0:
        heapq.heappush(heap_minus, -put);
    elif put == 0:
        if heap_minus and heap_plus:
            if heap_minus[0] > heap_plus[0]:
                print(heapq.heappop(heap_plus))
            else:
                print(-heapq.heappop(heap_minus))
        elif heap_minus:
            print(-heapq.heappop(heap_minus))
        elif heap_plus:
            print(heapq.heappop(heap_plus))
        else:
            print(put)
