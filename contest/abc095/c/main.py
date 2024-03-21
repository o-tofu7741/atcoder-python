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
    a, b, c, x, y = inp_li()
    ans = 10e5 * 2 * 5000
    print(min(a * x + b * y, (c * 2 * min(x, y))))


if __name__ == "__main__":
    main()
