#入力S取得
s = input()

#サーチする単語をリスト化
word = ['eraser', 'erase', 'dreamer', 'dream']

#Sからeraser, erase, dreamer, dreamの順にサーチして削除していく。（空文字に置き換え）
for i in word:
    s = s.replace(i, '')

#Sが空だったらYES、文字が残っていたらNOを出力
if len(s) == 0:
    print('YES')
else:
    print('NO')

