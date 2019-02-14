num = input()
s = list(map(int, input().split()))
# 最大値が10^9なので初期値を10にする
cnt = float("inf")

# sの各要素を2で割り続け、回数をカウントする
for x in s:
    temp = 0
    while x % 2 == 0:
        temp += 1
        x /= 2

    # ビットシフト回数をcntと比較し小さい方を代入
    if temp < cnt:
        cnt = temp

print(cnt)
