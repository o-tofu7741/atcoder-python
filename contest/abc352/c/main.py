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
    a = []
    b = []
    ab = []
    for i in range(n):
        ai, bi = inp_li()
        a.append(ai)
        b.append(bi)
        ab.append([bi - ai, i])
    ab.sort(reverse=True)
    mx, i = ab[0]
    print(sum(a) + mx)


if __name__ == "__main__":
    main()
