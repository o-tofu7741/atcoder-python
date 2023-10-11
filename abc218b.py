P = list(map(int, input().split()))
# for i in P:
#     print(chr(ord("a") - 1 + i), end="")
print("".join(list(map(lambda x: chr(ord("a") - 1 + x), P))))
