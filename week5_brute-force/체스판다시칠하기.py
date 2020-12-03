# 날짜: 2020/12/02
# 문제: 체스판 다시 칠하기 - 1018
# 문제요약: WBWB 로 구성된 문자열을 받아 완전한 체스판으로 고칠때 고쳐야하는 칸의 갯수를 구하라

def solution():
    wtht = input()
    heightCnt = int(wtht.split(" ")[0])
    widthCnt = int(wtht.split(" ")[1])
    chess = []
    fixCase1 = 0
    fixCase2 = 0

    for i in range(heightCnt):
        chess.append(input())
    
    first = chess[0][0]

    for i, line in enumerate(chess):
        for j, cell in enumerate(line):
            if (i+j) % 2 == 0 and white != cell: fixCase1 += 1
            elif (i+j) % 2 != 0 and white == cell: fixCase1 += 1
            if (i+j) % 2 == 0 and black != cell: fixCase2 += 1
            elif (i+j) % 2 != 0 and black == cell: fixCase2 += 1

    print(fixCase1, fi)

solution()