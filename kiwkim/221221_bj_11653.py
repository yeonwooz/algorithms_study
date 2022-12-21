#11653 소인수분해

import sys
from math import sqrt

readl = sys.stdin.readline


def prime(prime: int):
    div = 2
    while div < sqrt(prime):
        if prime % div == 0:
            return False
        div += 1
    return True    
def soinsu(number: int):
    tmp = number
    div = 1
    while div < sqrt(number) :
        div += 1
        if prime(div) and tmp % div == 0:
            print(div)
            tmp /= div
            div = 1
    if tmp > 1:
        print(int(tmp))
        
if __name__ == "__main__":
    number = readl()
    soinsu(int(number))

