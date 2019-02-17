#n,mを入力
n,m = map(int, input().split())

#suki = [[1,3],[1,2,3]]
suki = []
for i in range(n):
    suki.append(list(map(int, input().split())))

cnt = 0
j = 1
for j in range(m+1):
    for k in range(n):
        if suki[k][1:].count(j) == 0:
            break

        if k == (n-1):
            cnt += 1

print(cnt)
    
