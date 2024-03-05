import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys

# import numpy


def inp_i():
    return int(sys.stdin.readline().rstrip())


def inp_li():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def inp_s():
    return sys.stdin.readline().rstrip()


def inp_ls():
    return list(sys.stdin.readline().rstrip().split())


def main():
    n = inp_i()
    a = inp_li()
    ans = 0
    L = [0] * (n + 1)
    R = [0] * (n + 1)

    def my_gcd(x, y):
        return math.gcd(x, y)

    for i in range(n):
        print(L[i], a[i])
        L[i + 1] = my_gcd(L[i], a[i])
    for i in range(n - 1, -1, -1):
        print(R[i + 1], a[i])
        R[i] = my_gcd(R[i + 1], a[i])

    ans = 0
    for i in range(n):
        ans = max(ans, my_gcd(L[i], R[i + 1]))

    print(ans)
    # 1 8 12 4


if __name__ == "__main__":
    main()
