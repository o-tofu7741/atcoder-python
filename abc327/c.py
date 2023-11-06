import sys

A = []
for i in range(9):
    A.append(list(map(int, input().split())))

for i in range(9):
    if len(set(A[i])) != 9:
        print("No")
        sys.exit()
    if len(set([A[x][i] for x in range(9)])) != 9:
        print("No")
        sys.exit()
for i in range(3):
    for j in range(3):
        if (
            len(
                set(
                    A[i * 3][j * 3:j * 3 + 3]
                    + A[i * 3 + 1][j * 3:j * 3 + 3]
                    + A[i * 3 + 2][j * 3:j * 3 + 3]
                )
            )
            != 9
        ):
            print("No")
            sys.exit()
print("Yes")
