import sys
input = sys.stdin.readline

a, b = input().split()

cnt = 0
if (len(a) == len(b)):      # 길이가 같은 경우
    for i in range(len(b)): # 다른 문자의 개수 출력
        if(a[i] != b[i]):
            cnt += 1
    print(cnt)
else:                       # 길이가 다른 경우
    cnt_min = 51
    for i in range(len(b)-len(a)+1):    # b와 a의 길이의 차이만큼 반복해서, 다른 문자의 개수가 가장 작은 경우 찾기
        cnt = 0
        for j in range(len(a)):         # 다른 문자의 개수 세기
            if b[j+i] != a[j]:
                cnt += 1
        if cnt_min > cnt:               # 다른 문자의 개수의 min값 업데이트
            cnt_min = cnt
    print(cnt_min)

        
