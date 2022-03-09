a = int(input())

for i in range(a):
    h,w,n = map(int, input().split())
    num = n // h+1
    fl = n % h
    if n % h ==0:
        num = n // h
        fl = h
    print(f'{fl*100+num}')

        
     