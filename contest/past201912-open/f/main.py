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
    S = inp_s()
    ans = []
    flag = True
    i = 0
    for s in S:
        if s.isupper():
            if flag:
                flag = False
                ans += [s]
            else:
                flag = True
                i += 1
                ans[-1] += s
        else:
            ans[-1] += s
    print("".join(sorted(ans, key=str.lower)))


if __name__ == "__main__":
    main()
