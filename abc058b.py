Odd = list(input())
Even = list(input())
for i in range(len(Odd + Even)):
    print(Even.pop(0), end="") if i % 2 else print(Odd.pop(0), end="")
