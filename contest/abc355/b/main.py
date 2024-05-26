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
    n, m = inp_li()
    a = inp_li()
    b = inp_li()
    aa = []
    bb = []
    for i in a:
        aa.append((i, "a"))
    for j in b:
        bb.append((j, "b"))
    cc = sorted(aa + bb)
    prev = ""
    ans = "No"
    for v, ab in cc:
        if ab == "a" and prev == "a":
            ans = "Yes"
        prev = ab
    print(ans)


if __name__ == "__main__":
    main()
