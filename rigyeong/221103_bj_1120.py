import sys
str1, str2 = sys.stdin.readline().split()
ans = 51
if len(str1) == len(str2):
    cnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            cnt+=1
    print(cnt)
else:
    for i in range(len(str2)- len(str1)+1):
        cnt = 0
        for j in range(len(str1)):
            if str2[i+j] != str1[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)