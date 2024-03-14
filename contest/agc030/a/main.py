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
    a, b, c = inp_li()

    if a + b + 1 >= c:
        print(b + c)
    else:
        print(a + 2 * b + 1)


if __name__ == "__main__":
    main()
