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
    s = []
    c = []
    for i in range(n):
        si, ci = inp_ls()
        s.append(si)
        c.append(int(ci))
    ss = sorted(s)
    print(ss[sum(c) % n])


if __name__ == "__main__":
    main()
