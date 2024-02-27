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
    pi = [0] * (n + 1)
    for i in range(1, n + 1):
        pi[inp_i()] = i
    cnt = 1
    prev = pi[1]
    mx = 0
    for p in pi[1:]:
        if p > prev:
            cnt += 1
        else:
            cnt = 1
        mx = max(mx, cnt)
        prev = p
    print(n - mx)


if __name__ == "__main__":
    main()
