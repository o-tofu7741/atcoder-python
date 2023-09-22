P = list(map(int, input().split()))
for i in P:
    print(chr(ord("a") - 1 + i), end="")
# map(lambda x: print(chr(ord("a") - 1 + x), end=""), P)
