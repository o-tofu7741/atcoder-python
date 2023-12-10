# import bisect
# import collections
# import copy
# import heapq
# import itertools
# import math
# import string
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
    N, M = inp_li()
    S = inp_s()
    t = max(map(len, S.split("0")))
    logo = max(map(lambda x: x.count("2"), S.split("0")))
    m = N
    for s in S.split("0"):
        if len(s) == t:
            tmp = t - logo - M
            if tmp < 1:
                print(logo)
                sys.exit()
            elif tmp < m:
                m = tmp
    print(logo + m)


if __name__ == "__main__":
    main()
