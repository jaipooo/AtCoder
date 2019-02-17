#listに[a,b,c]形式で入力取得
box = list(map(int, input().split()))

#listの5と7の数をサーチする
#5が2個、7が2個ならYESを出力。違うならNO
if box.count(5) == 2 and box.count(7) == 1:
    print('YES')
else:
    print('NO')
