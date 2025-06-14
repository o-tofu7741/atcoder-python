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
    n = inp_i()
    A = inp_li()


    lst = [0]*n
    add = 0

    ans = A[:]

    for i in range(1, n):
        tmp = A[i - 1] - i
        if tmp < 0:
            add = 1




if __name__ == "__main__":
    main()
