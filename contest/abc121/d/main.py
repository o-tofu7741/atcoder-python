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


def xor(a):
    s = str(bin(a))[2:]
    ans = ""
    for i in range(len(s)):
        n = a + 1
        x = 2 ** (2 if i == 0 else i + 1)
        ni = n % x
        if i == 0:
            if ni > 1:
                ans = "1" + ans
            else:
                ans = "0" + ans
        elif ni <= x / 2:
            ans = "0" + ans
        elif ni % 2:
            ans = "1" + ans
        else:
            ans = "0" + ans
    return int(ans, 2)


def main():
    A, B = inp_li()
    print(xor(A - 1) ^ xor(B))


if __name__ == "__main__":
    main()
