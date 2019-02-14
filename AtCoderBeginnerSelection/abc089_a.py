#入力N, t,x,yを取得する。[[t1,x1,y1],[t2,x2,y2],…]という形式でリスト化する
n = int(input())

info = []
for i in range(n):
    info.append(list(map(int,input().split())))

#暫定段階でのプラン実行可能フラグ。プランが可能ならTrue
can_plan = False

#[t1,x1,y1]-[t2,x2,y2] = td, xd, yd変化量を取得する
for i in range(len(info)):
    if i == 0:
        td = info[i][0]
        xd = info[i][1]
        yd = info[i][2]
    else:
        if can_plan == True:
            td = info[i][0] - info[i-1][0]
            xd = info[i][1] - info[i-1][1]
            yd = info[i][2] - info[i-1][2]
        else:
            break
    
    # (x)+1(j回), (x)-1(k回), (y)+1(l回), (y)-1(m回)の組み合わせと個数の合計がtdと一致する組み合わせを検索する  
    #次のフェーズの検索をしていくので、プラン実行可能フラグはFalseにする
    can_plan = False

    for j in range(td+1):
        for k in range(td-j+1):
            for l in range(td-j-k+1):
                    m = td - j - k - l
                    if j*1+k*(-1) == xd and l*1+m*(-1) == yd:
                        can_plan = True

if can_plan == True:
    print('Yes')
else:
    print('No')