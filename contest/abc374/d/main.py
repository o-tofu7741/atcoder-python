import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
import sys

# import numpy

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
    n, s, t = inp_li()

    # [abcd,abcd,abcd,...]
    abcd = [list(map(lambda x: x + 0, inp_li())) for _ in range(n)]
    ans = INF

    # abcd_n = [(a,b,c,d),(a,b,c,d),(a,b,c,d),...]
    for abcd_n in itertools.permutations(abcd, n):
        for bits in range(2**n):
            tmp = 0
            prev_x = prev_y = 0
            for i in range(n):
                a, b, c, d = abcd_n[i]
                # 照準の移動時間
                # abスタート
                if (bits >> i) & 1:
                    tmp += math.sqrt((a - prev_x) ** 2 + (b - prev_y) ** 2) / s
                    prev_x = c
                    prev_y = d
                # cdスタート
                else:
                    tmp += math.sqrt((c - prev_x) ** 2 + (d - prev_y) ** 2) / s
                    prev_x = a
                    prev_y = b
                # レーザ照射時間
                tmp += math.sqrt((c - a) ** 2 + (d - b) ** 2) / t
            ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
