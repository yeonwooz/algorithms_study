import sys
input = sys.stdin.readline

n = int(input()) # n: 단어의 개수
words = []
for i in range(n):
    words.append(input().strip())

#print(words)
result = []
for i in range(len(words)):
    break_ = 0
    for j in range(len(words)):
        if i==j:
            continue
        if len(words[i]) > len(words[j]): # i가 접두사인지 판단
            continue
        else:
            flag = 0
            for k in range(len(words[i])): # 
                if words[i][k] == words[j][k]:
                    pass
                else:
                    flag = 1
                    break
            if flag == 0: # i가 접두사이면 for문 중단
                break_ = 1
                break
    if break_ == 1:
        pass
    else:
        result.append(words[i])
        
#set(result)
print(len(result))


# a = "hi"
# b = "hia"
# flag = 0
# for i in range(len(a)):
#     if a[i] == b[i]:
#         pass
#     else:
#         flag = 1
#         break
# print(flag)