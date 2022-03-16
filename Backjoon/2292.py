a = int(input())

nums = 1 #벌집의 개수
cnt =1

while a >nums: 
    nums += 6 *cnt #벌집이 6의 배수로 증가 -> 육각형이라
    cnt += 1
print(cnt)
    