def solution(left, right):
    answer = 0
    for i in range(left, right+1,1):
        c = 0
        for j in range(1, i+1):
            if i % j == 0:
                c += 1;  #약수: 개수 증가
        if c % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer