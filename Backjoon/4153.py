while True:
    n = list(map(int, input().split()))
    max_num = max(n)

    if sum(n) == 0:
        break
    n.remove(max_num)
     
    if n[0]**2 + n[1]**2 == max_num**2:
             print('right')
    else:
             print('wrong')