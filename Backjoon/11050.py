n,k = map(int, input().split())
f =1

for i in range(1, k+1):
    f *= ((n-i+1)/i)
print(int(f))
