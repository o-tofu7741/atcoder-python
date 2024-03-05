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


def change(s):
    if s == "a":
        return "b"
    elif s == "b":
        return "c"
    else:
        return "a"


def main():
    n = inp_i()
    s = inp_s()
    print(n, s)
    pts = collections.defaultdict(int)
    while set(s) != {"a"}:
        i = 0
        while s[i] != "a":
            i += 1
        pt = s[: i + 1]
        cnt = 0
        st = s[: i + 1]


if __name__ == "__main__":
    main()
