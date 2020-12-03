# 날짜: 2020/12/02
# 문제: 덩치 
# 문제요약: 입력받은 사람들의 키와 몸무게를 비교하여 등수를 출력하라

"""
풀이 - 1

비교결과를 승 무 패 로 나눠서 생각
승리시 + 1, 무승부시 0, 패배시 -1 를 부여해 점수를 환산
점수를 비교해 등수로 출력한다.
-> 점수 비교시 n의2승 만큼 순회를 더 해야 한다.

풀이 - 2

패배 횟수만 카운트, 비교를 마친뒤 패배 갯수로 등수를 계산하여 출력한다.
"""

# 비교하여 키와 몸무게가 모두 작을 경우 패배 카운트 +1
def compare(target, other):
    if target[0] < other[0] and target[1] < other[1]: return 1
    else: return 0

def solution():
    n = int(input())
    persons = []

    for i in range(n):
        info = list(map(int, input().split(" ")))
        persons.append(info)

    # 패배 한 횟수 + 1 이 그 사람의 등수가 된다
    for target in persons:
        loseCnt = 0
        for other in persons:
            loseCnt += compare(target, other)
        print(loseCnt + 1)

solution()