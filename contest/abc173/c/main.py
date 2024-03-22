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
    h, w, k = inp_li()
    cw = [inp_s() for _ in range(h)]
    b_all = sum([i.count("#") for i in cw])
    ans = 0
    for i in range(2**h):
        cw_chk = cw[:]
        b_n = b_all
        for i_h in range(h):
            if (i >> i_h) & 1:
                b_n -= cw_chk[i_h].count("#")
                cw_chk[i_h] = "-" * w

        for j in range(2**w):
            b_n2 = b_n
            cw_chk2 = ["".join(list(x)) for x in zip(*cw_chk)]
            for j_w in range(w):
                if (j >> j_w) & 1:
                    b_n2 -= cw_chk2[j_w].count("#")
                    cw_chk2[j_w] = "-" * h
            if b_n2 == k:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
