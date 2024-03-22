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
    a = inp_li()
    ans = INF
    for i in range(2 ** (n - 1)):
        a_split = []
        p = 0
        for j in range(n - 1):
            if (i >> j) & 1:
                a_split.append(functools.reduce(lambda x, y: x | y, a[p : j + 1]))
                p = j + 1
        a_split.append(functools.reduce(lambda x, y: x | y, a[p:]))
        ans=min(ans,functools.reduce(lambda x,y:x^y,a_split))
    print(ans)


if __name__ == "__main__":
    main()
