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
    souketa, kosu = inp_li()
    keta = [0] * kosu
    atai = [0] * kosu
    for i in range(kosu):
        keta[i], atai[i] = inp_li()
    ans = -1
    num = ["a"] * souketa
    for i in range(kosu):
        if keta[i] == 1 and atai[i] == 0 and souketa > 1:
            print(ans)
            sys.exit(0)
        else:
            if num[keta[i] - 1] == "a":
                num[keta[i] - 1] = str(atai[i])
            else:
                if num[keta[i] - 1] != str(atai[i]):
                    print(ans)
                    sys.exit(0)
    if souketa > 1 and num[0] == "a":
        num[0] = "1"
    print("".join(num).replace("a", "0"))


if __name__ == "__main__":
    main()
