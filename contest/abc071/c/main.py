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
    n = inp_i()
    a = inp_li()
    k1 = 0
    for k, v in sorted(collections.Counter(a).items(), reverse=True):
        if v > 3:
            if k1:
                print(k1 * k)
            else:
                print(k * k)
            exit()
        elif v > 1:
            if k1:
                print(k1 * k)
                exit()
            else:
                k1 = k
    else:
        print(0)


if __name__ == "__main__":
    main()
