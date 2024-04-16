import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import string
import sys

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
    n = inp_i()
    s = list(inp_s())
    target = "atcoder"

    # dp[0]はsを1文字も見てない時の各文字の可能な選択パターンの状態
    # dp[1:]になると、今見てるsの場所での、各文字の選択可能な数の状態
    # dp[][0]はカウント管理用のやつ
    # dp[][1:]はsのある場所を見てる時のtargetの各文字の選択可能な個数
    dp = [[0] * (len(target) + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(len(target) + 1):
            # 取り敢えず管理部分+各文字ごとに前回の状態を引き継ぎ
            dp[i + 1][j] += dp[i][j]

            # 同じ文字の時に、その文字の管理場所を更新
            if j < len(target) and s[i] == target[j]:
                dp[i + 1][j + 1] += dp[i][j]

    # でっかい数字を扱うのが苦手な言語の場合とか、厳しい問題の時は先のfor文の中のdp更新の時にmod(余り)取る必要あり
    # (x + y) % z も (x%z + y%z) % z も同じだから
    print(dp[n][len(target)] % (10**9+7))


if __name__ == "__main__":
    main()
