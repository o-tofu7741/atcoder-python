import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
import sys

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
    lr = []
    for i in range(n):
        lr.append(inp_li())
    ll = sorted(lr)
    rr = sorted(lr, key=lambda x: x[1])
    cnt = 0
    pl = pr = 0
    for i in range(n):
        l, r = ll[i]
        tmp = bisect.bisect_left(rr, r, key=lambda x: x[1])
        


if __name__ == "__main__":
    main()
