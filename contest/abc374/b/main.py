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
    s = inp_s()
    t = inp_s()
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            print(i + 1)
            return
    else:
        if len(s) == len(t):
            print(0)
        else:
            print(min(len(s), len(t)) + 1)


if __name__ == "__main__":
    main()
