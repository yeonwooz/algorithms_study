#20365 블로그2
import sys
input = sys.stdin.readline

N = int(input())

lst = list(input().strip())

cnt_blue = 0
cnt_red = 0

if lst[0] == 'B': prev = 1
elif lst[0] == 'R' : prev = 0

for e in lst:
    if prev:
        if e == 'R': 
            cnt_blue += 1
            prev = 0
    else:
        if e == 'B': 
            cnt_red += 1
            prev = 1


if lst[-1] == 'B': cnt_blue += 1
else: cnt_red += 1

if cnt_blue >= cnt_red : print (cnt_red+1)
else : print(cnt_blue+1)

# 더 줄이기 -> 블루 레드 따로 셀 필요 없이 그냥 바뀌는 횟수만 세면 됩니다!
# import sys
# readl = sys.stdin.readline
# putnum = int(readl())
# putstr = readl().strip()
# prev = putstr[0]
# cnt= 1
# for char in putstr:
#     if prev != char:
#         if char != putstr[0]:
#             cnt += 1
#             prev = char
#         else:
#             prev = char
# print(cnt)
