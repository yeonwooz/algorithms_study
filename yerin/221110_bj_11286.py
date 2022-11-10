# 11286 절댓값 힙
import sys
import heapq
input = sys.stdin.readline

N = int(input())

pos_heap = [] # 양수 힙
neg_heap = [] # 음수 힙 

for i in range (N):
    x = int(input())
    if x == 0 : # 절대값이 가장 작은 원소 출력하기
        if not pos_heap and not neg_heap: # 두 힙이 다 비어있으면 : 0 출력
            print (0)
        elif not neg_heap: # 음수 힙이 비어있으면 : 양수 힙에서 pop, 최소값
            print (heapq.heappop(pos_heap))
        elif not pos_heap: # 양수 힙이 비어있으면 : 음수 힙에서 pop, -최소값 출력
            print (heapq.heappop(neg_heap))
        else: 
            if pos_heap[0] < neg_heap[0]: # 양수 힙에 최소값이 있다면 : 양수 힙에서 pop, 최소값 출력
                print (heapq.heappop(pos_heap)) 
            else: # 음수 힙에 최소값이 있다면 : 음수 힙에서 pop, -최소값 출력
                print ((-1)*heapq.heappop(neg_heap)) 
    elif x > 0: # x가 양수면 양수 힙에 push
        heapq.heappush(pos_heap, x)
    else : # x가 음수면 음수 힙에 push
        heapq.heappush(neg_heap, -x)
        