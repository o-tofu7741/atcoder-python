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
    h = inp_i()
    memo = collections.defaultdict(int)
    print(attack(h, memo))


def attack(h, memo):
    if h == 0:
        return 0
    elif memo[h] != 0:
        return memo[h]
    else:
        return 1 + attack(h // 2, memo) * 2


if __name__ == "__main__":
    main()
