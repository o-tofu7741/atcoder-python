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
    a, b = inp_li()
    ans = [0] * 3
    ans[a - 1] = 1
    ans[b - 1] = 1
    if a == b:
        print(-1)
    else:
        for i in range(3):
            if ans[i] == 0:
                print(i + 1)


if __name__ == "__main__":
    main()
