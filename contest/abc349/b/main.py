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
    s = inp_s()
    c = collections.Counter(s)
    cnt = collections.defaultdict(int)
    for i, v in c.items():
        cnt[v] += 1
    for i,v in cnt.items():
        if v!=2:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
