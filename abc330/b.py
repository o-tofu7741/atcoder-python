N, L, R = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for a in A:
    if a <= L:
        ans.append(str(L))
    elif L < a < R:
        ans.append(str(a))
    else:
        ans.append(str(R))
print(" ".join(ans))
