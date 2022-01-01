#행렬 뎃셈, 뺄셈

def solution(arr1, arr2):
    a_sum =[]
    answer = []
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            a_sum.append(arr1[i][j] + arr2[i][j])
        answer.append(a_sum)
        a_sum =[]
    return answer