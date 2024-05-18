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
    a = sorted(inp_li(), reverse=True)
    t2 = [2 ** (30 - t) for t in range(30)]
    ans = 0

    a_d = collections.defaultdict(int)
    for i in a:
        a_d[i] += 1

    # 重複を除いた各要素について、大きい順2べきリストt2を見ていく
    uniq_lst = [i for i in a_d.keys()]
    for i in uniq_lst:
        for t in t2:
            # ペア候補iがすでに使われてる場合と、tがiより小さい==ペアはいない時
            if a_d[i] == 0 or t < i:
                break
            # iのペアの数字
            j = t - i
            tmp = 0
            if i == j:
                tmp = a_d[i] // 2
            else:
                # jがいなければ0が返るから問題ナシ
                tmp = min(a_d[i], a_d[j])
            a_d[i] -= tmp
            a_d[j] -= tmp
            ans += tmp

    print(ans)


if __name__ == "__main__":
    main()
