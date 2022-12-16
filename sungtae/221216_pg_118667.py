# 프로그래머스 두 큐 합 같게 만들기
from collections import deque

def solution(queue1, queue2):
    q1_s = sum(queue1)
    q2_s = sum(queue2)
    total_sum = q1_s + q2_s
    # 예외처리: 합이 2의 배수가 아닌 경우 
    if total_sum%2 != 0:        
        return -1
    
    total_queue = queue1 + queue2
    total_max = max(total_queue)
    # 예외처리: 한명의 크기가 절반보다 큰 경우
    if total_max > total_sum/2: 
        return -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    answer = 0
    limit = (len(queue1) + len(queue2))*2
    while(1) :     
        # 같으면 성공
        if q1_sum == q2_sum:    
            break
        # q1이 큰 경우
        elif q1_sum > q2_sum:   
            a = q1.popleft()
            q2.append(a)
            q1_sum -= a
            q2_sum += a
            answer += 1
        # q2가 큰 경우
        else:                   
            a = q2.popleft()
            q1.append(a)
            q1_sum += a
            q2_sum -= a
            answer += 1
        if answer >= limit: # 이 이상 하면 안돌아가는거임
            answer = -1
            break
    return answer