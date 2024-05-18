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
    a = inp_li()
    ans = 0
    now = 0
    q = collections.deque(a)
    while q:
        i = q.popleft()
        if now + i > k:
            now = i
            ans += 1
        else:
            now += i
    if now:
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
