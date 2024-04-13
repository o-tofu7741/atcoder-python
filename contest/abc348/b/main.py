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
    xy = [inp_li() for _ in range(n)]
    for i in range(n):
        mx = 0
        index = i
        x1, y1 = xy[i]
        for j in range(n):
            x2, y2 = xy[j]
            sqrt = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            if sqrt > mx:
                mx = sqrt
                index = j
        print(index + 1)


if __name__ == "__main__":
    main()
