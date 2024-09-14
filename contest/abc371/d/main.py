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
    n =inp_i()
    x = inp_li()
    p = inp_li()
    acm = [0] + p
    for i in range(n):
        acm[i+1] += acm[i]
    q =inp_i()
    for _ in range(q):
        l,r=inp_li()
        li = bisect.bisect_left(x,l)
        ri = bisect.bisect_right(x,r)
        print(acm[ri]-acm[li])



if __name__ == "__main__":
    main()
