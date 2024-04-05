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
    h, w, a, b = inp_li()
    room = [[1] * h for _ in range(w)]
    ans = 0

    def rec(a, b, x, y):
        if a < 0 or b < 0:
            return

        if x > w or y > h:
            return


if __name__ == "__main__":
    main()
