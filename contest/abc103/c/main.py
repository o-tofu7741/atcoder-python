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
    a = inp_li()
    # ans = 0
    # for i in a:
    #     ans += i - 1
    # print(ans)
    m = math.lcm(*a) - 1
    print(sum(map(lambda x: m % x, a)))


if __name__ == "__main__":
    main()
