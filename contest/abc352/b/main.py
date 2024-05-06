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
    s = inp_s()
    t = inp_s()
    j = 0
    ans = []
    for i in s:
        while t[j] != i:
            j += 1
        ans.append(j + 1)
        j += 1
    print(*ans)


if __name__ == "__main__":
    main()
