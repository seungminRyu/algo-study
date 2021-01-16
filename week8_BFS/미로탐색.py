# 날짜: 2021.01.14
# 문제: 미로탐색 - 2178
# 문제요약: 미로의 끝 지점 까지 가는데 걸리는 최소 카운트를 구하라
from collections import deque

def solution():
    n, m = map(int, input().split(' '))
    maze = [input() for _ in range(n)]
    # for _ in range(n): maze.append( list( map( int, list(input() ) ) ) )

    q = deque()
    q.append((0,0))
    distance = [[0] * m for _ in range(n)]
    print(distance)
    distance[0][0] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        # 좌표이동
        for dx, dy in (-1,0), (1,0), (0,-1), (0, 1):
            nx, ny = x+dx, y+dy
            # 좌표범위 조사
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if maze[ny][nx] == '1' and distance[ny][nx] == 0:
                distance[ny][nx] = distance[y][x] + 1
                q.append((nx,ny))
    
    print(distance[n-1][m-1])

solution()