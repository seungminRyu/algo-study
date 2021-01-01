# 날짜: 2020.12.09
# 문제: 별찍기 - 2447
# 문제요약: 
"""""""""""""""""""""
n = 3
widthIndex  = 0
heightIndex = 0

n = 9
widthIndex = 0
heightIndex = 0
widthIndex = 3
heightIndex = 0
widthIndex = 6
heightIndex = 0
*********
* ** ** *
*********
***   ***
* *   * *
***   ***
*********
* ** ** *
*********

n = 27
...
"""""""""""""""""""""

# 풀이: 재귀함수내에서 수행할 동작 -> 조건을 충족하면 줄바꾸기, 특정조건에서 중간은 출력 X
def createStar(n):
    createStar(n//3)
    for i in range(3):
        for j in range(3):
            if (i == 1 and j == 1):
                continue
            else:
                star[widthIndex+i][heightIndex+j] = 1

def printStar(starArr):
    _starArr = starArr
    
def solution():
    n = int(input())
    for i in range(n):
        line = []
        for j in range(n):
            line.append(0)
        star.append(line)

    createStar(27)
    print(star)


star = []
solution()