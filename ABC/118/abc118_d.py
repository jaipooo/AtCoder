ini = [[1, 2], [2, 5], [3, 5], [4, 4], [5, 5], [6, 6], [7, 3], [8, 7], [9, 6]]

n,m = map(int, input().split())
num = list(map(int, input().split()))

table = []

for i in range(m):
    table.append(ini[num[i]-1])

table = sorted(table, key=lambda x:x[1])

for i in range(m):
    while num > table[m][1]:
        num = num % table[m][1]
