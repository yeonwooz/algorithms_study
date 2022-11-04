# 1120 문자열
import sys
from itertools import permutations
input = sys.stdin.readline

A, B = input().split()

dif_len = len(B) - len(A)

if dif_len == 0:
    dif_min = 0
    for i in range(len(B)):
        if A[i]!= B[i]:
            dif_min += 1
    print(dif_min)
else:
    dif_min = 51
    for i in range (dif_len+1):
        cnt = 0
        for j in range (len(A)):
            if B[j+i] != A[j]:
                cnt += 1 
        dif_min = min(dif_min, cnt)
    print(dif_min)
