# import bisect
# import collections
# import copy
# import heapq
# import itertools
# import math
# import string
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
    h, w = inp_li()
    a = [list(inp_s()) for _ in range(h)]
    n = inp_i()
    rce = [[0] * w for _ in range(h)]
    for _ in range(n):
        r, c, e = inp_li()
        rce[r - 1][c - 1] = e
    pt = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    prevs_ = [[0] * w for _ in range(h)]

    def rec(e, i, j, prevs):
        # print(i + 1, j + 1, e)
        if a[i][j] == "T":
            print("Yes")
            exit()
        else:
            for pi, pj in pt:
                ni = i + pi
                nj = j + pj
                if (
                    0 <= ni < h
                    and 0 <= nj < w
                    and prevs[ni][nj] == 0
                    and a[ni][nj] != "#"
                    and e > 0
                ):
                    prevs1 = prevs[:]
                    prevs1[ni][nj] = 1
                    # print(ni, nj)
                    rec(
                        rce[ni][nj] if rce[ni][nj] > e - 1 else e - 1,
                        ni,
                        nj,
                        [tmp[:] for tmp in prevs1],
                    )

    for i in range(h):
        for j in range(w):
            if a[i][j] == "S":
                prevs_[i][j] = 1
                break
        else:
            continue
        break
    rec(rce[i][j], i, j, prevs_)
    print("No")


if __name__ == "__main__":
    main()
