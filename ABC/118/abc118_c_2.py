def resolve():
    #モンスター数
    n = int(input())

    #モンスターiの体力:mon[i]
    mon = list(map(int, input().split()))

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a%b)

    ans = mon[0]
    for i in range(1,n):
        ans = gcd(ans,mon[i])

    print(ans)

resolve()