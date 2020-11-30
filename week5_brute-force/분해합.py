# 날짜: 2020/11/30
# 문제: 분해합 - 2231
# 문제 요약: 256은 245와 245의 각 자리 수를 더한 값이다 이때 245를 256의 생성자라 한다. 자연수 N이 주어 졌을 때 N의 가장 작은 생성자를 구하라.

"""
풀이 - 1

1부터 주어진 숫자 전까지 순회하며 생성자에 부합하는 숫자를 구한다.
"""

def solution():
    n = int(input())
    didFind = False

    # n보다 작은 수를 모두 순회
    for i in range(1, n):
        sumN = i
        # 각 자리 수를 더하기 위해 문자열로 만들어 각 자리 수를 더한다.
        for char in str(i):
            sumN += int(char)
        
        # 생성자를 못 찾은 경우 0출력을 위해 didFind에 발견 여부를 저장한다.
        if (sumN == n):
            didFind = True
            print(i)
            break # 가장 작은 값을 찾았을때 for문을 나온다.
    
    if (didFind == False):
        print(0)

solution()