A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
b = [int(input()) for i in range(N)]

for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            A[i][j] = 0

ans = "No"
if (A[0][0] + A[1][1] + A[2][2]) == 0 or (A[0][2] + A[1][1] + A[2][0]) == 0:
    ans = "Yes"
i = 0
while i < 3 and ans != "Yes":
    if sum(A[i]) == 0 or (A[0][i] + A[1][i] + A[2][i]) == 0:
        ans = "Yes"
    i += 1
print(ans)
