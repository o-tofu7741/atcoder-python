N, K, P = map(int, input().split())
AC = []
for i in range(N):
    AC.append(list(map(int, input().split())))

ans = [0, 0, 0, 0]
while ans[1] < P or ans[2] < P or ans[3] < P:
    if ans[1] < P:
        pass
