n = int(input())

#モンスターiの体力:mon[i]
mon = list(map(int, input().split()))


zero = 0
while mon.count(0) != (n-1):
    mon.sort()
    min = mon[zero]
    tei = zero + 1
    for i in range(tei,n):
        mon[i] = mon[i] % min
        if mon[i] == 0:
            zero += 1
mon.sort()
print(mon[zero])
