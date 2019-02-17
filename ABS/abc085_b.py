n = int(input())
d = []

for i in range(n):
    d.append(int(input()))

#昇順にソート
d.sort()

current_max = 0
cnt = 0

#前の要素より大きければ、現在参照値を更新し、cntを増やす
for i in d:
    if i > current_max :
        current_max = i
        cnt += 1

print(cnt)