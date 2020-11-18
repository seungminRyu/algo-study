# 작성 날짜 : 20201116
# 작성자 : 유 승 민
# 문제 명 : k번째 수
# 문제 유형: 정렬

def solution():
    conditions = list(map(int ,list(input().split(" "))))

    maxNum = conditions[0]
    k = conditions[1]

    ls = list(map(int ,list(input().split(" "))))
    ls.sort()

    print(ls[k-1])

solution()
