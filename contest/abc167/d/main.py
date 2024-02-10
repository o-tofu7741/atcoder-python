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
    N, K = inp_li()
    A = inp_li()
    passed = collections.defaultdict(int)
    passed[0] = 1
    next = A[0] - 1
    points = [0]

    # 繰り返される文字列をシミュレーションで見つける
    # 1回だけしか通らないところと、2回通るところを見つける
    while passed[next] < 2:
        # print(next, passed, points)
        passed[next] += 1
        points.append(next)
        next = A[next] - 1

    # 重複・非重複を数える
    dup = sum(map(lambda x: (x == 2), passed.values()))
    not_dup = len(points) - dup * 2

    # Kが重複までのテレポート回数以下の時はKを、
    # それ以外の時は重複を外して最終位置を求める
    # print(dup, not_dup, (K - not_dup) % dup)
    ans = K if K <= dup + not_dup else (not_dup + (K - not_dup) % dup)
    print(points[ans] + 1)


if __name__ == "__main__":
    main()
