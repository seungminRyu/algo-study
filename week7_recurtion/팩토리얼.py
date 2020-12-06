# 날짜: 2020.12.07
# 문제: 팩토리얼 - 10872
# 문제요약: 수를 입력 받아 수의 팩토리얼을 구하라

def factorial(n, i, facN):
    if(n < i):
        return facN 
    facN *= i
    return factorial(n, i+1, facN)

def solution():
    n = int(input())
    
    facN = factorial(n, 1, 1)
    print(facN)

solution()
