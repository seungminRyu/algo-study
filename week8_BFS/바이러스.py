# 날짜: 2021.01.15
# 문제: 바이러스
# 문제요약: 여러 대의 컴퓨터가 연결되있을 때 바이러스가 걸리게 되는 컴퓨터의 수를 구하라
from collections import deque

def solution():
    num = int(input())
    cnct = int(input())
    # 인접 노드를 저장할 리스트
    adj = [[] for _ in range(num)]
    # 노드별 방문 여부
    visited = [False for _ in range(num)]

    for _ in range(cnct):
        a, b = map(int, input().split())
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)

    print(adj)
    print(visited)

    q = deque()
    q.append(0)
    visited[0] = True
    cnt = 0

    while q:
        virus = q.popleft()
        for com in adj[virus]:
            if not visited[com]:
                visited[com] = True
                q.append(com)
                cnt += 1
    print(cnt)

solution()