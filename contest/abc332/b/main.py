# import bisect
# import collections
# import copy
# import heapq
# import itertools
# import math
# import string
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
    K, G, M = inp_li()
    g = m = 0
    for i in range(K):
        if g == G:
            g = 0
        elif m == 0:
            m = M
        else:
            if m <= G - g:
                g += m
                m = 0
            else:
                m -= G - g
                g = G
    print(g, m)


if __name__ == "__main__":
    main()
