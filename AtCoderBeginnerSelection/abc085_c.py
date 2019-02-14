n,y = map(int, input().split())

discover = False

y = y// 1000

for i in range(n+1):
    for j in range(n-i+1):
        k = n-i-j
        if k>=0 and y==i*10+j*5+k*1:
            discover = True
            break

    if discover == True:
        break


if discover == True:
    print(i,j,k)
else:
    print(-1,-1,-1)
