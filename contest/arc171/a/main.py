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
    C = [inp_li() for _ in range(inp_i())]
    for c in C:
        n, a, b = c
        ans = "No"
        if a <= n:
            if b <= (n - a) ** 2:
                if a == 0 and b <= ((n - a) // 2 + (n - a) % 2) * (n - a):
                    ans = "Yes"
                else:
                    if a == n // 2 or a == n // 2 + 1:
                        ans = "Yes"
                    else:
                        pass

        print(ans)


if __name__ == "__main__":
    main()
