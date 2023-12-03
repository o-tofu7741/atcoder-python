n, t = input().split()
n = int(n)
s = []
for i in range(n):
    s.append(input())

ans = []
if t in s:
    ans.append(s.index(s))  # += [i for i, x in enumerate(s) if x == t]
tn = len(t)
for i, str in enumerate(s):
    c = 0
    for j in str:
        if j != 

print(f"{len(ans)}\n{' '.join(ans)}")
