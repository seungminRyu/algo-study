# 날짜: 2020/11/22
# 문제: 수 찾기 - 1920
# 문제 요약: 정수 배열을 받고 또 다른 정수 배열을 한 개 더 받는다. 두번째 배열에 있는 수들이 첫번째 배열에 있는지를 조사한다.

def binary_search_recursion(target, start, end, data):
    if start > end:
        return 0

    mid = (start + end) // 2

    if data[mid] == target:
        return 1
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binary_search_recursion(target, start, end, data)

def solution():
    numsLen = int(input())
    numList = list(map(int, input().split(" ")))
    numList.sort()
    targetsLen = int(input())
    targetList = list(map(int, list(input().split(" "))))

    for target in targetList:
        result = binary_search_recursion(target, 0, numsLen-1, numList)
        print(result)

solution()