N, L, R = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for a in A:
    for x in range(L, R + 1):
        for y in range(L, R + 1):
            if abs(x - a) <= abs(y - a):
                pass
            else:
                break
        else:
            ans.append(str(x))
print(" ".join(ans))
