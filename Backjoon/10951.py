while True:
    try:
            a,b = map(int, input().split())
            0<a and 10>b
            print(a+b)
    except:
        break