K = int(input())


def calc_321(n):
    N = str(n)
    (ans := True) if len(N) == 1 else (ans := False)
    if ans == False:
        for i in range(len(N) - 1):
            if int(N[i]) > int(N[i + 1]):
                ans = True
            else:
                ans = False
                break
    return ans


i = c = 0 
while c < K:
    i += 1
    if calc_321(i):
        c += 1
print(i)
