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
    ans = 0
    p1 = p2 = p3 = 0
    for i in range(n):
        s = inp_s()
        ans += s.count("AB")

        if s[0] == "B" and s[-1] == "A":
            p1 += 1
        elif s[-1] == "A":
            p2 += 1
        elif s[0] == "B":
            p3 += 1
    m = 1 if p1 > 0 else 0
    print(ans + p1 // 2 + min(p2 + m, p3 + m))


if __name__ == "__main__":
    main()
