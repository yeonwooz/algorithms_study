# 맞았습니다!!
import sys
from collections import deque
n = int(sys.stdin.readline())
words = [(sys.stdin.readline().strip()) for _ in range(n)]
words.sort()
q = deque()
for word in words:
    if q:
        len_q_word = len(q[-1])
        if q[-1] in word[:len_q_word]:
            q.pop()
    q.append(word)
print(len(q))