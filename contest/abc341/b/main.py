# import bisect
# import collections
# import copy
# import heapq
import itertools

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
    n = inp_i()
    a = inp_li()
    s = []
    t = []
    for _ in range(n - 1):
        si, ti = inp_li()
        s.append(si)
        t.append(ti)
    accm_s = [0] + list(itertools.accumulate(s))
    accm_t = [0] + list(itertools.accumulate(t))
    sum_a = sum(a) - a[-1]
    while True:
        cnt = 0
        for i in range(n - 1):
            if (sum_a + accm_t[-2] - accm_t[i]) < (accm_s[-1] - accm_s[i]):
                break
            if a[i] >= s[i]:
                a[i] -= s[i]
                a[i + 1] += t[i]
                sum_a += t[i] - s[i]
            else:
                cnt += 1
        else:
            if cnt == n - 1:
                break
            else:
                continue
        break
    print(a[n - 1])


if __name__ == "__main__":
    main()
