#nを入力する
n = int(input())

#Lを入力する
l = list(map(int,input().split()))


#max<他の合計の場合YES,
mx = max(l)
if mx < sum(l)-mx:
    print('Yes')
else:
    print('No')