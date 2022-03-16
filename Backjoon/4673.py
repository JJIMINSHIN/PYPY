# 1부터 10000까지 숫자 저장
n = set(range(1, 10001))

#셀프 넘버가 아닌 수 저장
n_set= set()

for i in range(1, 10001): 
    for j in str(i): #숫자를 문자열로 변환 | 123 => 123+1+2+3
         i += int(j) ## d(i) = i + j1 + j2 + j3 + .. = 123+1+2+3
    n_set.add(i) #셀프넘버 아닌 수 저장

#셀프 넘버만 있는 set = 전체 set - 셀프 넘버 아닌 set
set_n = n - n_set 

#오름차순으로 정렬 후 출력
for i in sorted(set_n): 
    print(i)