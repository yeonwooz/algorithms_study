# 블로그2
import sys
input = sys.stdin.readline

n = int(input()) # n: 색을 칠해야 하는 문제의 수 
rb = input().strip()

prev = rb[0]
cnt = 1
for char in rb:
    if prev != char:
        if char != rb[0]:
            cnt += 1
            prev = char
        else:
            prev = char
print(cnt)


        
        