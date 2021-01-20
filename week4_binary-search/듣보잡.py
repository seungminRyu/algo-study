# 날짜: 2020/11/25
# 문제: 듣보잡 - 1764
# 문제 요약: 듣도 못한 사람, 보도 못한 사람 리스트가 주어질때 듣도 보도 못한 사람 찾기

"""
방법 - 1

두 배열을 모두 정렬,
이분 탐색을 구현하여 첫번째 배열을 돌며 target을 설정
두번째 배열에서 이분탐색으로 target을 찾는다.

방법 - 2

해쉬를 활용하여 입력 받을때 마다 값을 1증가
값이 1이상일 경우 출력
"""

def binarySearch(target, start, end, data):
    if start > end:
        return 0

    mid = (start + end) // 2

            if data[mid] == target:
         return data[mid]
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binarySearch(target, start, end, data)

def solution():
    arr = list(map(int, input().split(" ")))
    n = arr[0]
    m = arr[1]
    nList = []
    mList = []
    START = 0
    END = m-1
    find = []

    for i in range(n):
        nList.append(input())

    for i in range(m):
        mList.append(input())
    mList.sort()

    for target in nList:
        result = binarySearch(target, START, END, mList)
        if not (result == False):
            find.append(result)

    print(len(find))
    for a in find:
        print(a)

solution()
def binarySearch(target, start, end, data):
    if start > end:
        return 0

    mid = (start + end) // 2

    if data[mid] == target:
        return data[mid]
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binarySearch(target, start, end, data)

def solution():
    arr = list(map(int, input().split(" ")))
    n = arr[0]
    m = arr[1]
    nList = []
    mList = []
    START = 0
    END = m-1
    find = []

    for i in range(n):
        nList.append(input())

    for i in range(m):
        mList.append(input())
    mList.sort()

    for target in nList:
        result = binarySearch(target, START, END, mList)
        if not (result == False):
            find.append(result)

    print(len(find))
    for a in find:
        print(a)

solution()