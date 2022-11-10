import sys
readl = sys.stdin.readline

lens = int(readl())
lst = []
for i in range(lens):
    lst.append(int(readl()))

lst.sort()
count = 4
maxcount = 5   
cha = 5
for i in range(1, lens):
    if (lst[i] - lst[i-1]) < cha:
        cha = lst[i] - lst[i-1]
        count -= 1
    else:
        if count < maxcount:
            cha = 5
            maxcount = count
            count = 4
if count < maxcount:
            maxcount = count
            count = 4
print(maxcount)