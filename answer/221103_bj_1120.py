# 백준 1120 문자열 해답
import sys
input = sys.stdin.readline

A, B = input().split()

dif_min = 51
for i in range (len(B)-len(A)+1):
    cnt = 0
    for j in range (len(A)):
        if B[j+i] != A[j]:
            cnt += 1 
    dif_min = min(dif_min, cnt)
    
print(dif_min)