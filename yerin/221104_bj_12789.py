# 12789 도키도키 간식드리미
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
waitings = deque(map(int, input().split()))
stack = deque()

cnt = 1
while waitings or stack:
    if waitings:  # 대기열에 사람이 있는 경우
        if waitings[0] == cnt: # 대기열의 왼쪽에 있는 사람 차례인 경우
            waitings.popleft()
            cnt = cnt + 1
            continue
        if stack:
            if stack[-1] == cnt: # 스택의 가장 위에 있는 사람 차례인 경우
                stack.pop()
                cnt = cnt + 1
                continue
        stack.append(waitings.popleft()) # 대기열 왼쪽 또는 스택의 탑에 차례인 사람이 없는 경우 
    elif stack: # 대기열에서 사람이 다 빠지고, 스택에만 사람이 있는 경우
        if stack[-1] == cnt: 
            stack.pop()
            cnt = cnt + 1
        else: break 

# 결과 출력
if cnt == N+1 : print("Nice") 
else: print("Sad")