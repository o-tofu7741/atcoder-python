# import bisect
# import collections
# import copy
# import heapq
# import itertools
# import math
# import string
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
    N, K = inp_li()
    a = N // K
    b = 0

    if K % 2 == 0:
        b = N // K
        if K // 2 <= N % K:
            b += 1
    print(a**3 + b**3)


if __name__ == "__main__":
    main()
