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


def f(x, y):
    return (x + y) % 10**8


def main():
    n = inp_i()
    a = list(map(lambda x: x % 10**8, inp_li()))
    m = 10**8
    ans = 0
    for i in range(n - 1):
        tmp = 0
        for j in range(i + 1, n):
            tmp += f(a[i], a[j])
        ans += tmp
    print(ans)


if __name__ == "__main__":
    main()
