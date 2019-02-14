n,y = map(int, input().split())

discover = False

y = y// 1000

for i in range(y//10+1):
    for j in range(y//5+1):
        for k in range(y//1+1):
            if y==i*10+j*5+k*1 and n==i+j+k:
                discover = True
                break
        if discover == True:
            break

    if discover == True:
        break


if discover == True:
    print(i,j,k)
else:
    print(-1,-1,-1)
