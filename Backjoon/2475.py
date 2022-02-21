n = list(map(int, input().split()))
res=0

for i in n:
    res += i*i
print(res%10)