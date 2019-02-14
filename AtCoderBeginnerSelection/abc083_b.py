n,a,b = map(int, input().split())

#該当する数を代入していく
sum = 0

#各桁の和をいれる
tmp_sum = 0

for i in range(1, n+1):
    tmp_sum = 0
    tmp = i

    for j in range(4):
        tmp_sum += tmp % 10
        tmp = tmp // 10

    if tmp_sum>=a and tmp_sum<=b:
        sum += i

print(sum)