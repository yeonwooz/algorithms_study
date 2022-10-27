import sys
readl = sys.stdin.readline

size = int(readl().strip())
strarr = []

for i in range(size):
    strarr.append(readl().strip())
ret_set = set()

for str1 in strarr:
    for str2 in strarr:
        if str1 in str2:
            break;
        elif str1 != str2:
            ret_set.add(str1)
print(ret_set)