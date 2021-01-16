# 날짜: 2020.01.14
# 문제: 단지번호붙히기
# 문제요약: 같은 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

def solution():
    n = int(input())
    area = []
    for _ in range(n): area.append( list( map( int, list(input() ) ) ) )

    