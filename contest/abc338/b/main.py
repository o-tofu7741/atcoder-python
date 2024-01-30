# import bisect
import collections

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
    s = inp_s()
    c = collections.Counter(s)
    d = c.most_common()
    ans = [i[0] for i in d if i[1] == d[0][1]]
    print(sorted(ans)[0])


if __name__ == "__main__":
    main()
