#1141 접두사 예린
import sys
input = sys.stdin.readline
N = int(input())
str_lst = [ input().strip() for _ in range (N) ]

result_set = set()

for s1 in str_lst:
    Flag = 0
    for s2 in str_lst:
        if s1 == s2: continue
        elif s2.startswith(s1):
            Flag = 1
            break
    if Flag == 0: result_set.add(s1)

print(len(result_set))