M, D = map(int, input().split())
y, m, d = map(int, input().split())
if d == D:
    d = 1
    if m == M:
        m = 1
        y += 1
    else:
        m += 1
else:
    d += 1
print(f"{y} {m} {d}")
