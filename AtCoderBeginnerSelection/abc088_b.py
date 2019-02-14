n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

sum_a = sum(a[0::2])
sum_b = sum(a[1::2])

print(sum_a-sum_b)