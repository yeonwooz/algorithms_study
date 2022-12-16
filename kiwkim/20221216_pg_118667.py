import sys
from collections import deque
input = sys.stdin.readline


def solution(queue1, queue2):
    import queue
    from collections import deque
    dequeue1 = deque(queue1)
    dequeue2 = deque(queue2)
    
    sum1 = sum(dequeue1)
    sum2 = sum(dequeue2)
    
    if (sum1 + sum2) % 2 == 1:
        return -1
    elif sum1 == sum2:
        return 0
    cnt = 0
    limit = (len(dequeue1) + len(dequeue2)) * 2
    for i in range(limit):
        if sum1 == sum2:
            return cnt
        cnt += 1
        if sum1 > sum2:
            pop1 = dequeue1.popleft()
            dequeue2.append(pop1)
            sum1 -= pop1
            sum2 += pop1
        else:
            pop2 = dequeue2.popleft()
            dequeue1.append(pop2)
            sum1 += pop2
            sum2 -= pop2            
    return cnt

