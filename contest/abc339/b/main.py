import bisect
import collections
import copy
import heapq
import itertools
import math
import pprint
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
    H, W, N = inp_li()
    ans = [["."] * W for i in range(H)]
    h = w = 0
    t = 0
    for _ in range(N):
        if ans[h][w] == ".":
            ans[h][w] = "#"
            if t == 0:
                w = (w + 1) % W
            elif t == 1:
                h = (h + 1) % H
            elif t == 2:
                w = (w - 1) % W
            else:
                h = (h - 1) % H
            t = (t + 1) % 4
        else:
            ans[h][w] = "."
            if t == 0:
                w = (w - 1) % W
            elif t == 1:
                h = (h - 1) % H
            elif t == 2:
                w = (w + 1) % W
            else:
                h = (h + 1) % H
            t = (t - 1) % 4
        # print("\n".join(["".join(i) for i in ans]))
        # print()
    print("\n".join(["".join(i) for i in ans]))


if __name__ == "__main__":
    main()
