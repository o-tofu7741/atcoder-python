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
    s = list(inp_s())
    t = list(inp_s().lower())
    for i in range(3):
        if t[i] in s:
            s[: s.index(t[i]) + 1] = []
            # print(s)
            # print(t[i])
        elif i == 2 and t[i] == "x":
            continue
        else:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
