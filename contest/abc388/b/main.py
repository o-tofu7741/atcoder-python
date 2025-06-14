import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
import sys

# import numpy

INF = 10**18


def inp_i():
    return int(sys.stdin.readline().rstrip())


def inp_li():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def inp_s():
    return sys.stdin.readline().rstrip()


def inp_ls():
    return list(sys.stdin.readline().rstrip().split())


def main():
    n, d = inp_li()
    tl = [inp_li() for _ in range(n)]

    for k in range(1, d + 1):
        ans = 0
        for i in range(n):
            t, l = tl[i]
            tmp = t * (l + k)
            if ans <= tmp:
                ans = tmp
        print(ans)


if __name__ == "__main__":
    main()
