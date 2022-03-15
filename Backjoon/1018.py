n, m = map(int, input().split())
board = []
cnt=[]
# 입력한 데이터를 리스트에 저장
for _ in range(n):
    board.append(list(map(str, input())))

# 리스트를 8*8로 쪼개기
for i in range(0, n-7):
    for j in range(0, m-7):
        idx1 = 0
        idx2 = 0
        # 8*8 보드를 하나씩 검사하기
        for x in range(i, i+8):
            for y in range(j, j+8):
                # 인덱스 합이 짝수인 경우 일정한 색 가지게 됨.
                if (x+y) % 2 == 0:
                    # 0,0 값이 B인 경우
                    if board[x][y] != 'W':
                        idx1 += 1
                    # 0,0 값이 W인 경우
                    if board[x][y] != 'B':
                        idx2 += 1
                # 인덱스 합이 홀수인 경우 일정한 색
                else:
                    # 0,0 값이 W인 경우
                    if board[x][y] != 'W':
                        idx2 += 1
                    # 0,0 값이 B인 경우
                    if board[x][y] != 'B':
                        idx1 += 1
        cnt.append(idx1)
        cnt.append(idx2)

print(min(cnt))