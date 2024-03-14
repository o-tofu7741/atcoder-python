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
    n, k = inp_li()
    s = []
    for i in range(n):
        a, b = inp_li()
        s.append(a-b)
        s.append(b)
    s.sort(reverse=True)
    print(sum(s[:k]))


if __name__ == "__main__":
    main()
