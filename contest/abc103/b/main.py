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
    S = input()
    T = input()

    ans = "No"
    for i in range(len(S)):
        if T == (S[i:] + S[:i]):
            ans = "Yes"
            break

    print(ans)


if __name__ == "__main__":
    main()
