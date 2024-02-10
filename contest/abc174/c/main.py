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
    K = inp_i()

    # 7の数字がKの倍数 = 7がKで割り切れる = 7の数字 % K が 0
    # 7の数字%Kが0になる数字を探す
    lst = [7 % K]

    # K回分回すだけで足りるのはなぜか？
    # 1.数字をKで割った余りの全パターンはK-1個
    # 2.出てきた余りすべてで、(10 * 一個前の余り + 7) % Kで次の余りが示せるので、一回でも出てきた余りと同じ数字が次の余りとして出てきたらループが始まるから
    # よって、K回分回して余り0に出会えなかったらどっかでループしてるからなしになる
    # ループしてなかったらK回分回してるのでどちらにしろK-1のどこかにある0を見つけられるからok
    for i in range(K):
        # a(x) % y と a(x%y) % y は同じ
        # (x+a) % y と (x%y + a) % y も同じ
        lst.append((10 * lst[-1] + 7) % K)
    ans = -1
    for i in range(K):
        if lst[i] == 0:
            ans = i + 1
            break
    print(ans)


if __name__ == "__main__":
    main()
