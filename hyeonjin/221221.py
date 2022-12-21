import sys
import math

input = sys.stdin.readline
n = int(input())


def is_prime(n):
    root = int(math.sqrt(n))
    i = 2

    while i <= root:
        if n % i == 0:
            return False

        i += 1

    return True


def solution(n):
    root = int(math.sqrt(n))
    i = 2

    while (n > 1) and (i <= root):
        if is_prime(i):
            while n % i == 0:
                print(i)
                n //= i

        i += 1

    if n > 1:
        print(n)


solution(n)
