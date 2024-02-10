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
    N=inp_i()
    C = inp_s()
    ans = 0
    wr=-1
    for i in range(N-1):
        if C[i]+C[i+1]=="WR":



if __name__ == "__main__":
    main()
