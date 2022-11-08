#에너지 드링크 홍리경
#https://www.acmicpc.net/problem/20115

import sys
n = int(sys.stdin.readline())
energy = list(map(int, sys.stdin.readline().split()))
print((sum(energy)+max(energy))/2)