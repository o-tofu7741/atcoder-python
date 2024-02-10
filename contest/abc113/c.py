ken_num, shi_num = map(int, input().split())
ken_year = []
for i in range(shi_num):
    ken_year.append(list(map(int, input().split())))
ken_year.sort(key=lambda x: x[1])
