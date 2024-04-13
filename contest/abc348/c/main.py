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
    c = collections.defaultdict(lambda: 10**9)
    for i in range(n):
        a, ci = inp_li()
        if c[ci] > a:
            c[ci] = a
    print(max(c.values()))


if __name__ == "__main__":
    main()
