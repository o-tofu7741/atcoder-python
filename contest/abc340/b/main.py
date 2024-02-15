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
    q = inp_i()
    a = []
    for _ in range(q):
        i, j = inp_li()
        if i == 1:
            a.append(j)
        else:
            print(a[-j])


if __name__ == "__main__":
    main()
