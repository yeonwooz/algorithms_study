#11286 절댓값 힙

import sys
import heapq
readl = sys.stdin.readline
## 음수 힙과 양수 힙을 따로 만들고 출력 연산시. 두 힙의 루트를 비교해서 더 절댓값이 작은 놈을 출력.
n = int(readl())
heap_minus = [] ## 음수
heap_plus = [] ## 양수
cnt = 0
for i in range(n):
    put = int(readl())
    if put > 0:
        heapq.heappush(heap_plus, put); 
    elif put < 0:
        heapq.heappush(heap_minus, -put); ## 음수는 음수 곱해서 넣음.
    elif put == 0:
        if heap_minus and heap_plus:
            if heap_minus[0] > heap_plus[0]:
                print(heapq.heappop(heap_plus)) 
            else:
                print(-heapq.heappop(heap_minus)) ## 음수힙팝 음수 곱해서 팝함
        elif heap_minus:
            print(-heapq.heappop(heap_minus))
        elif heap_plus:
            print(heapq.heappop(heap_plus))
        else:
            print(put)
