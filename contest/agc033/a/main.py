# import bisect
import collections

# import copy
# import functools
# import heapq
# import itertools
# import math
# import string
import sys

# import numpy

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
    h, w = inp_li()
    a = [list(inp_s()) for _ in range(h)]
    q = collections.deque([])
    ans = 0
    pt = ((0, 1), (1, 0), (-1, 0), (0, -1))
    checked = [0] * h

    while True:
        fin = 0
        for y in range(h):
            if checked[y]:
                fin += 1
                continue
            cnt = 0
            for x in range(w):
                if a[y][x] == "#":
                    q.append((x, y))
                elif a[y][x] == "-":
                    continue
                else:
                    cnt += 1
            if cnt == 0:
                checked[y] = 1
                fin += 1
        if fin == h:
            break
        while len(q) > 0:
            bx, by = q.popleft()
            for px, py in pt:
                if (
                    (0 <= bx + px < w)
                    and (0 <= by + py < h)
                    and a[by + py][bx + px] == "."
                ):
                    a[by + py][bx + px] = "#"
            a[by][bx] = "-"
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
