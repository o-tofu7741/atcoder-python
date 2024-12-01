import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
import sys

# import numpy

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
    n, d = inp_li()
    s = list(reversed(inp_s()))
    for i in range(n):
        if s[i] == "@":
            d -= 1
            s[i] = "."
        if d <= 0:
            break
    print("".join(reversed(s)))



if __name__ == "__main__":
    main()
