#N,Lを入力より取得する
n,l = map(int, input().split())

#リストに[s1,s2,...,sn]形式で取得
slist = []
for i in range(n):
    slist.append(input())
"""
if 'a' < 'd':
    print('1')
else:
    print('0')

"""
#リストの要素を辞書早い順にソートする
"""

for i in range(n):
    j = i + 1
    for j in range(n):
        for k in range(l):
            if slist[i][k] < slist[j][k]:
                slist[i], slist[j] = slist[j],slist[i]
                break
            elif slist[i][k] > slist[j][k]:
                break
"""
# sortでstrのリストを辞書順にソートできる
slist.sort()
out = ''.join(slist)

#最終結果を出力
print(out)