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


class MinMaxList:
    def __init__(self, itr):
        self.set_lst = sorted(itr)
        self.minimum = self.set_lst[0]
        self.maximum = self.set_lst[-1]

    def min(self):
        return self.minimum

    def max(self):
        return self.maximum

    def remove(self, value):
        self.set_lst.discard(value)
        if self.minimum > value:
            self.minimum = value

    def add(self, value):
        self.set_lst.add(value)


def main():
    n, k = inp_li()
    p = inp_li()
    dp = [0] * (n)
    for i in range(n):
        dp[p[i] - 1] = i
    ans = INF
    wide = set(dp[:k])
    for i in range(n - k):
        ans = min(ans, max(wide) - min(wide))
        wide.add(dp[i + k])
        wide.discard(dp[i])
    print(ans)


if __name__ == "__main__":
    main()
