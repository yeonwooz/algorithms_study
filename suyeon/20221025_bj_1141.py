#started at 10:31
n = int(input())

wordset = set()
for _ in range(n):
    wordset.add(input().rstrip())

words = list(wordset)
words.sort(key=len)

def is_prefix(stra,strb):
    # a가 더 짧음
    cnt = 0
    for i in range(len(stra)):
        if stra[i] != strb[i]:
            break
        cnt +=1
    return cnt == len(stra)

# removeset = set()
for i in range(len(words)):
    for j in range(i+1, len(words)):
        if is_prefix(words[i], words[j]):
            removeset.add(j)
# 끝에서부터 탐색해서 지워야할듯
for idx in removeset:
    print(idx)
    if words[]
