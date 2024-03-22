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
    s = inp_s()
    a, b, c, d = inp_li()
    ss = []
    tmp = s[0]
    for i in s[1:]:
        if tmp[-1] == i:
            ss.append(tmp)
            tmp = i
        else:
            tmp += i
    ss.append(tmp)
    print(ss)


if __name__ == "__main__":
    main()
