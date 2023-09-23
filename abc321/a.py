N = input()

(ans := "Yes") if len(N) == 1 else (ans := "No")
if ans == "No":
    for i in range(len(N) - 1):
        if int(N[i]) > int(N[i + 1]):
            ans = "Yes"
        else:
            ans = "No"
            break

print(ans)
