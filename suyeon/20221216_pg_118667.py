from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total = sum(queue1) + sum(queue2)
    if (total) % 2 > 0:
        return -1
    limit = (len(queue2) + len(queue1)) * 2    
    
    cnt = 0
    while (sum1 != sum2):
        if sum1 > sum2:
            el = queue1.popleft()
            queue2.append(el)
            sum1 -= el
            sum2 += el
        elif sum1 < sum2:
            el = queue2.popleft()
            queue1.append(el)
            sum2 -= el
            sum1 += el
        else:
            break
        if cnt == limit:
            cnt = -1
            break
        cnt += 1
        
    if (sum1 == sum2): 
        return cnt
    return -1