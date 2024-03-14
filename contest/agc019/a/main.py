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
    q, h, s, d = inp_li()
    n = inp_i()

    money1 = [4 * q, 2 * h, s]
    money2 = [i * 2 for i in money1] + [d]

    money1.sort()
    money2.sort()

    if n % 2 == 1:
        print(n // 2 * money2[0] + money1[0])
    else:
        print(n // 2 * money2[0])


if __name__ == "__main__":
    main()
