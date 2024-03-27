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
    n = inp_i()
    f = [inp_li() for _ in range(n)]
    p = [inp_li() for _ in range(n)]
    ans = -INF
    for i in range(1, 2**10):
        profit = 0
        cnt = [0] * n
        for day_time in range(10):
            if (i >> day_time) & 1:
                for shop_i, shop_v in enumerate(f):
                    if shop_v[day_time]:
                        cnt[shop_i] += 1
        for c_i, c_v in enumerate(cnt):
            profit += p[c_i][c_v]
        ans = max(ans, profit)
    print(ans)


if __name__ == "__main__":
    main()
