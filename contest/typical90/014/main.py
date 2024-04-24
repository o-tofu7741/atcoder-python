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
    n = inp_i()
    a = inp_li()
    b = inp_li()
    ans = 0
    for i, j in zip(sorted(a), sorted(b)):
        ans += abs(i - j)
    print(ans)


if __name__ == "__main__":
    main()
