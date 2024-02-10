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
    x = inp_i()

    # 任意の面を表に出来るので、理想の数値連続パターンは 5・6 になる
    ans = x // 11 * 2

    # 11の剰余を見て、必要な回数分さいころを振る
    if x % 11 > 0:
        ans += 1
        if x % 11 > 6:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
