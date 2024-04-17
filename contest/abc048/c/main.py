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
    n, x = inp_li()
    a = inp_li()

    # 答え
    result = 0

    # 先頭要素のみ x からの超過分を先に食べる
    if a[0] > x:
        result += a[0] - x
        a[0] = x

    # 左端から見ていく
    for i in range(n - 1):
        if a[i] + a[i + 1] > x:
            # a[i]+a[i+1]のx超過分を食べる
            result += a[i] + a[i + 1] - x
            a[i + 1] = x - a[i]

            


if __name__ == "__main__":
    main()
