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
    A, B, N = inp_li()

    # いつだって大きいのは、floor(x/B)が0になる時で、尚且つxが出来るだけ大きい時
    # なのでB未満かつ、N以下の値がxの最適な値になる
    n = B - 1 if B <= N else N
    print(A * (n) // B - A * ((n) // B))


if __name__ == "__main__":
    main()
