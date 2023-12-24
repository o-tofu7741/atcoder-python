import collections

n = int(input())
a = tuple(map(int, input().split()))

ans = []
a_c = collections.Counter(a)
accm = {}
sort_ac = dict(sorted(a_c.items(), reverse=True))
tmp = 0
for k, v in sort_ac.items():
    accm[k] = tmp
    tmp += k * v

for a_i in a:
    ans.append(str(accm[a_i]))
print(*ans)
