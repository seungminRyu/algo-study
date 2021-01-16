# 날짜: 2020.01.14
# 문제: 토마토
# 문제요약: 인접한 토마토가 모두 익을때까지 걸리는 시간 출력, 모두 익을수 없는 상황은 -1, 이미 모두 익은 상태는 0

from collections import deque

def solution():
    n, m = list( map( int, input().split() ) )
    box = []
    for _ in range(m): box.append(list( map( int, input().split() ) ) )

    riped = deque()
    notRiped = 0
    date = 0

    # 익은 토마토의 위치, 날짜값 riped에 저장
    for i in range(m):
        for j in range(n):
            if box[i][j] == 1: riped.append([i, j, 0])
            if box[i][j] == 0: notRiped += 1
    
    # 이미 모두 다 익은경우
    if notRiped == 0:
        print(0)
        return
    
    while riped:
            toma = riped.popleft()
            date = toma[2]
            
            # 다음 위치로 이동 가능한 경우를 체크하고 수행
            if toma[0] < m-1 and box[toma[0]+1][toma[1]] == 0:  # 토마토 밑으로
                box[toma[0]+1][toma[1]] = 1
                riped.append([toma[0]+1, toma[1], toma[2]+1])
                notRiped -= 1
            if toma[0] > 0 and box[toma[0]-1][toma[1]] == 0:    # 토마토 위로
                box[toma[0]-1][toma[1]] = 1
                riped.append([toma[0]-1, toma[1], toma[2]+1])
                notRiped -= 1
            if toma[1] < n-1 and box[toma[0]][toma[1]+1] == 0:  # 토마토 오른쪽으로
                box[toma[0]][toma[1]+1] = 1
                riped.append([toma[0], toma[1]+1, toma[2]+1])
                notRiped -= 1
            if toma[1] > 0 and box[toma[0]][toma[1]-1] == 0:    # 토마토 왼쪽으로
                box[toma[0]][toma[1]-1] = 1
                riped.append([toma[0], toma[1]-1, toma[2]+1])
                notRiped -= 1
    if notRiped:
        print(-1)
    else:
        print(date)
            
solution()