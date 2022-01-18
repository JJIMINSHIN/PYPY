num = int(input())
n = num
cnt = 0

while True:
    a= n//10
    b =n%10
    c= (a+b)%10
    n = (b*10)+c 
    cnt += 1
    if(num == n):
        break
print(cnt)