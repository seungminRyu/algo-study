# 날짜: 2020/11/29
# 문제: 블랙잭 - 2798
# 문제 요약: n장의 카드가 써져 있는 숫자가 주어졌을 때, m을 넘지 않으면서 최대한 가까운 카드 3장의 합을 출력하라

"""
문제 해결

3개를 뽑는 경우를 모두 구해 배열에 저장하는데, 합이 m을 넘을 경우 저장하지 않는다.
저장한 값 중 가장 큰 값을 출력한다.

1. 3개를 모두 뽑는 경우 구현...

방법 1: index i, j, k를 활용한 3중 반복문
방법 2: 재귀 함수로 구현, 한 가지 원소를 뽑고 그 원소를 제외한 리스트로 조합을 구한다.
"""
def combination(lst, n):
    ret = []
    # 뽑는 숫자 n이 배열의 갯수 보다 클경우
    if n > len(lst): return ret

    # 뽑는 숫자 n이 1일 경우
    if n == 1:
        for i in lst:
            ret.append([i])

    # 뽑는 숫자 n이 1 보다 클경우
    elif n > 1:
        for i in range(len(lst)-n+1):
            for temp in combination(lst[i+1:], n-1):
                ret.append([lst[i]] + temp)

    return ret

def soulution():
    n, m = map(int, input().split())
    valueArr = list(map(int, input().split()))
    sumValueLst = []

    # 3개를 뽑은 경우의 수에서 합이 m을 넘지 않는 것만 리스트에 추가한다.
    for case in combination(valueArr, 3):
        sumValue = case[0] + case[1] + case[2]
        if sumValue <= m:
            sumValueLst.append(sumValue)

    # 합한 값의 리스트에서 가장 큰 값을 리턴
    print(max(sumValueLst))

soulution()
