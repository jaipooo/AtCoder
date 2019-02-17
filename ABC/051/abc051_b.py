#k,sを入力から取得する
k,s = map(int, input().split())

#2重forでx,y,zを探索する。組み合わせを見つけるたびにcntを+1していく
cnt = 0
for x in range(k+1):
    for y in range(k+1):
        z = s - x - y
        if 0 <= z <= k:
            cnt += 1
        
#組数を出力する
print(cnt)