# 백준 11286
# 절댓값 힙
import sys
import heapq
from collections import deque
input = sys.stdin.readline

n = int(input()) # n: 연산의 개수
heap = []

for i in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(heap, (abs(a), a))   # 우선순위1-절댓값, 우선순위2-실제값
    else:
        if not heap: # heap이 비어있는 경우
            print(0)
        else:
            print(heapq.heappop(heap)[1]) # 실제값 기준으로 pop

