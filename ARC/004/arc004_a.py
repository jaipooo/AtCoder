#入力からnを得る
n = int(input())

#[x0,y0]...[xn-1,yn-1]を入力から得る
position = []
for i in range(n):
    position.append(list(map(int, input().split())))

#0と1...n-1を比較、1と2...n-1を比較・・・を繰り返し、差分x＋差分yがmaxとなる2つのindexを得る
max_difference = 0
max_index = []
for i in range(n):
    j = i + 1
    for j in range(n):
        difference = abs(position[i][0]-position[j][0])+abs(position[i][1]-position[j][1])
        if difference > max_difference:
            max_difference = difference
            max_index = [i,j]

#2点間の距離を計算し出力する
distance = ((position[max_index[0]][0]-position[max_index[1]][0])**2+(position[max_index[0]][1]-position[max_index[1]][1])**2)**0.5
print(distance)