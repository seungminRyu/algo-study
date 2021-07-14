"""
5
    4
        3
            2
            1
        2
            1
            0

    3
        2
            1
            
            0
        1
"""
# 날짜: 2020.01.26
# 문제: 피보나치 함수
# 문제요약: n번째 피보나치 수를 구하는 함수에서 1과 0을 호출하는 횟수를 구하라
cnt1 = 0
cnt0 = 0

def fibonacci(n):
    global cnt1, cnt0
    if n == 1:
        cnt1 += 1
        return 1
    elif n == 0:
        cnt0 += 1
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def solution():
    n = int(input())
    arr = []
    for _ in range(n): arr.append(int(input()))

    for num in arr:
        global cnt1, cnt0
        fibonacci(num)
        print(cnt0, cnt1)
        cnt1 = 0
        cnt0 = 0

solution()

