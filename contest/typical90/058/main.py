import bisect
import collections
import copy
import heapq
import itertools
import math
import string
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

    # 愚直にシミュレーションしてるとクソでかい数字でTLEする
    # 無駄な計算発生パターンは、Kがありえんぐらい大きくて、計算後のNが0にならない数字の時
    # 過去に同じNが出てきてたら同じ変遷をたどるので、過去に存在した値かのチェックをする
    num = []
    while N not in num and K > 0:
        num.append(N)
        N += sum(map(int, str(N)))
        N %= 100000
        K -= 1

    # 最終的なNの値は、繰り返しが始まったところのインデックス番号+残りの回数%パターンの長さ
    # # K=0の時は繰り返しパターンを見つけられてないので、現在のNの値を返す
    print(num[num.index(N) + K % (len(num) - num.index(N))] if K else N)


if __name__ == "__main__":
    main()
