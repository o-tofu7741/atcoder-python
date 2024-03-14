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
    a, b, k = inp_li()
    if k >= a:
        k -= a
        a = 0
        if k >= b:
            k -= b
            b = 0
        else:
            b -= k
    else:
        a -= k
    print(a, b)


if __name__ == "__main__":
    main()
