import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
import sys

sys.setrecursionlimit(10**6)

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
    s = inp_s()
    n = len(s)
    pt = ["dream", "dreamer", "erase", "eraser"]
    pn = list(map(len, pt))
    dp = [False] * n

    def rec(i):
        result = False
        for j in range(4):
            if s[i - pn[j] : i] == pt[j]:
                if rec(i - j):
                    result = True
        return result

    print(rec(n))


if __name__ == "__main__":
    main()
