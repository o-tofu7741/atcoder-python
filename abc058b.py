Odd = list(input())
Even = list(input())
# for i in range(len(Odd + Even)):
#     print(Even.pop(0) if i % 2 else Odd.pop(0), end="")
print([a + b for a in Even for b in Odd])
