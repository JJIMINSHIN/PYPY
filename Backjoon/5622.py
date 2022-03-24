alp = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
n = input()

t = 0

for i in alp :  
    for j in i:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in n :  # 입력받은 문자를 하나씩 분리
            if j == x :  # 두 알파벳이 같으면
                t += alp.index(i) +3  # t = t + index +3
print(t)