a = int(input())

for i in range(a):
    h,w,n = map(int, input().split())
    f = 0
    hn = 0
    if n % h == 0:
        f = h*100
        hn = n // h
    else:
        f = (n%h)*100
        hn = 1 + n//h
    print(f+hn)
        
     