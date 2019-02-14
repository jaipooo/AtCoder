n,a,b = map(int, input().split())
tmp = list(str(n))
nl = [0,0,0,0]
nl = list(str(n))

length = len(tmp)
if(length==1):
    nl = ['0', '0', '0']
    nl.extend(tmp)
elif length==2:
    nl = ['0', '0']
    nl.extend(tmp)
elif length==3:
    nl = ['0']
    nl.extend(tmp)
else:
    nl = tmp

cnt = 0
fin = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if( (i + j + k + l >= a) and (i + j + k + l <= b) ):
                    cnt = cnt + i*1000 + j*100 + k*10 + l 
                
                if( (i==int(nl[0])) and (j==int(nl[1])) and (k==int(nl[2])) and (l==int(nl[3])) ):
                    fin = 1
            
                if(fin ==1):
                    break
            
            if(fin ==1):
                break
        
        if(fin ==1):
            break
            
    if(fin ==1):
        break


print(cnt)
