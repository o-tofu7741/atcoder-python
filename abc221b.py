S = input()
T = input()

(ans := "No") if S != T else (ans := "Yes")
for i in range(len(S) - 1):
    s = list(S)
    s[i], s[i + 1] = s[i + 1], s[i]
    if T == "".join(s):
        ans = "Yes"

print(ans)
