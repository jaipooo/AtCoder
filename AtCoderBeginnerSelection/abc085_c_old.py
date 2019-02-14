n,y = map(int, input().split())

discover = False

for i in range(y//10000+1):
    for j in range(y//5000+1):
        for k in range(y//1000+1):
            if y==i*10000+j*5000+k*1000 and n==i+j+k:
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
