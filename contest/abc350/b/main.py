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
    n, q = inp_li()
    t = inp_li()
    for k, v in collections.Counter(t).items():
        if v % 2 == 1:
            n -= 1
    print(n)


if __name__ == "__main__":
    main()
