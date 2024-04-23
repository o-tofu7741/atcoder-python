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
    a = []
    b = []
    for _ in range(n):
        ai, bi = inp_li()
        a.append(ai)
        b.append(bi)
    ans = 0
    for ai, bi in zip(reversed(a), reversed(b)):
        if bi == 1 or ((ans + ai) % bi) == 0:
            continue
        ans += bi - ((ans + ai) % bi)
    print(ans)


if __name__ == "__main__":
    main()
