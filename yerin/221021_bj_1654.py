# 1654 랜선 자르기
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

lines = [ int(input()) for _ in range (N) ]

start = 1
end = max(lines)

while start <= end:
    mid = (start + end) // 2
    num_of_lines = 0
    for line in lines:
        num_of_lines += line // mid
    if num_of_lines >= K :
        max_length = mid 
        start = mid + 1
    else:
        end = mid -1

print(max_length)