# 날짜: 2020/12/02
# 문제: 영화감독 숌 - 1436
# 문제요약: 666이 들어간 수를 작은 수부터 나열했을때 n번째 수를 찾아라

'''
풀이

666 1666 2666 3666
...
6661 6662 6663 6664
...
7666 8666 9666 10666

'''

def solution():
    n = int(input())
    num = 666
    i = 0

    while(True):
        _num = str(num)
        if '666' in _num:
            i += 1
            if i == n:
                print(num)
                break
        num += 1

solution()
