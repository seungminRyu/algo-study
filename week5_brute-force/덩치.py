# 날짜: 2020/12/02
# 문제: 덩치 
# 문제요약: 상대보다 키, 몸무게가 모두 클 경우 덩치가 큼. 상대보다 키, 몸무게가 모두 작을 경우 덩치가 작음. 둘의 경우를 제외한 경우 같은 등수. 입력받은 사람들의 등수를 출력하라

"""
풀이 - 1

비교결과를 승 무 패 로 나눠서 생각
승리시 + 1, 무승부시 0, 패배시 -1 를 부여해 점수를 환산
점수를 비교해 등수로 출력한다.
-> 점수 비교시 n의2승 만큼 순회를 더 해야 한다.

풀이 - 2

패배 횟수만 카운트, 비교를 마친뒤 패배 갯수로 등수를 계산하여 출력한다.
"""

def compare(target, other):
    if target[0] < other[0] and target[1] < other[1]: return 1
    else: return 0

def solution():
    n = int(input())
    persons = []

    for i in range(n):
        info = list(map(int, input().split(" ")))
        persons.append(info)

    for target in persons:
        loseCnt = 0
        for other in persons:
            loseCnt += compare(target, other)
        print(loseCnt + 1)

solution()