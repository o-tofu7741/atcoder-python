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
    n, l = inp_li()
    x = set(inp_li())
    t1, t2, t3 = inp_li()
    dp = [0] * (l + 1)
    i=0
    while i <= l:
        c1 = dp[i-1] + t1 + (t3 if i in x else 0)
        c2 = 


if __name__ == "__main__":
    main()
