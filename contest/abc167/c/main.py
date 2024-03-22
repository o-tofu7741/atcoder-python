import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys

# import numpy

inf = 10**18


def inp_i():
    return int(sys.stdin.readline().rstrip())


def inp_li():
    return list(map(int, sys.stdin.readline().rstrip().split()))


def inp_s():
    return sys.stdin.readline().rstrip()


def inp_ls():
    return list(sys.stdin.readline().rstrip().split())


def main():
    n, m, X = inp_li()
    ca = [inp_li() for _ in range(n)]
    mn = inf
    for i in range(2**n):
        a = [0] * m
        cost = 0
        for j in range(n):
            if (i >> j) & 1:
                a = [(x + y) for x, y in zip(a, ca[j][1:])]
                cost += ca[j][0]
        # print(i, cost, a)
        if all(map(lambda x: x >= X, a)):
            mn = min(mn, cost)
    if mn == inf:
        mn = -1
    print(mn)


if __name__ == "__main__":
    main()
