# import bisect
# import collections
# import copy
# import heapq
import itertools
import math

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
    n, p, q = inp_li()
    print(
        sum(
            map(
                lambda x: 1 if math.prod(x) % p == q else 0,
                itertools.combinations(inp_li(), 5),
            )
        )
    )


if __name__ == "__main__":
    main()
