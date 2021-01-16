from itertools import combinations, permutations

def solution():
    N = int(input())
    memberNum = N//2

    mat = [[0] * (N+1)] + [list(map(int, ("0 " + input()).split())) for _ in range(N)]
    print(mat)
    minAb = 1000

    for team1 in combinations(range(1, N+1), memberNum):
        # team2 만들기
        team2 = []
        for i in range(1, N+1):
            if i not in team1:
                team2.append(i)

        ab1 = 0
        ab2 = 0
        # team1 점수계산 
        for e in permutations(team1, 2):
            ab1 += mat[e[0]][e[1]]

        # team2 점수계산 
        for e in permutations(team2, 2):
            ab2 += mat[e[0]][e[1]]

        d = abs(ab1 - ab2)
        if d < minAb:
            minAb = d

    print(minAb)

solution()
