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


def get_x(lst, n):
    if n == 1:
        return 0
    else:
        if lst[n] != 0:
            return lst[n]
        else:
            lst[n] = n + get_x(lst, n // 2) + get_x(lst, -(-n // 2))
            return lst[n]


def main():
    n = inp_i()
    lst = collections.defaultdict(int)
    print(get_x(lst, n))


if __name__ == "__main__":
    main()
