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
    n, k = inp_li()
    h = inp_li()
    dp = [INF] * n
    dp[0] = 0
    for i in range(n - 1):
        for j in range(i, i + k + 1):
            if j >= n:
                break
            dp[j] = min(dp[j], abs(h[i] - h[j]) + dp[i])
    print(dp[n - 1])


if __name__ == "__main__":
    main()
