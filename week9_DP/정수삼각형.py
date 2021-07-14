# 날짜: 2020/01/20
# 문제: 정수 삼각형
# 문제 요약: 정수로 이루어진 삼각형에서 정수를 더하며 내려올때, 거쳐간 숫자의 합이 가장 큰 경우를 찾아라

"""
1. 
s1-1 = s1[0]

2. 
s2-1 = s2[0] + s1-1
s2-2 = s2[1] + s1-1

3.
s3-1 = s3[0] + s2-1

s3-2 = s3[1] + s2-1
s3-3 = s3[1] + s2-2

s3-4 = s3[2] + s2-2

4.
s4-1 = s4[0] + s3-1

s4-2 = s4[1] + s3-1
s4-3 = s4[1] + s3-2
s4-4 = s4[1] + s3-3

s4-5 = s4[2] + s3-2
s4-6 = s4[2] + s3-3
s4-7 = s4[2] + s3-4

s5-8 = s4[3] + s3-4

5. 

"""

def solution():
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

    l = len(triangle)
    s = [[] for x in range(l) ]

    for n, floor in enumerate(triangle):
        for i, num in enumerate(floor):
            if i == 0:
                s[n][0] = s[n-1][0] + num
            elif i == n:
                s.append(s[i] + num)
            else:
                a = s[i-1] + num
                b = s[i] + num
                
                a > b  s[i] = a : s[i] = b

    print(s)

solution()