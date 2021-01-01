# 날짜: 2020.12.09
# 문제: 피보나치수 - 10870
# 문제요약: 재귀호출을 사용해 n번째 피보나치수를 출력하라

# 재귀호출할 때 PreVal은 prePreVal로, presentVal은 preVal로 전달된다.
def fibonacci(n, prePreVal, preVal, i):
    presentVal = prePreVal + preVal
    
    if (i == n):
        return presentVal

    return fibonacci(n, preVal, presentVal, i+1)

def solution():
    n = int(input())
    startIndex = 2

    if (n == 0): print(0)
    elif (n == 1): print(1)
    else: print(fibonacci(n, 0, 1, startIndex))

solution()
