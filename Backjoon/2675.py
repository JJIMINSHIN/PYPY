t = int(input())

for i in range(t):
    n,s = list(map(str,input().split()))
    n = int(n)
    
    for i in s:
        print(n*i, end="")
    print()