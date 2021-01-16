from itertools import permutations

def solution():
    N = int(input())
    numList = list(map(int, input().split()))
    getOperator = list(map(int, input().split()))
    dic = {0: "+", 1: "-", 2: "*", 3:"//"}
    operationTmp = []
    sumList = []
    stack = []


    for i in range(4):
        for j in range(getOperator[i]):
            operationTmp.append(dic[i])
            
    operationList = set(permutations(operationTmp, N - 1))

    for operation in operationList:

        tmp = str(numList[0])
        stack.append(tmp)
        
        # 연산자, 숫자 하나씩 추가
        for i in range(N - 1):
            stack.append(operation[i])
            stack.append(str(numList[i + 1]))

            if operation[i] == "//":
                
                # ??
                if int(stack[0]) < 0 and int(stack[2]) > 0:
                    stack[0] = str(-int(stack[0]))
                    
                elif int(stack[0]) > 0 and int(stack[2]) < 0:
                    stack[2] = str(-int(stack[2]))

            if len(stack) == 3:
                tmp = (eval("".join(stack)))
                stack = [str(tmp)]
                
            if i == N - 2:
                sumList.append(int(tmp))
                stack = []

    print(max(sumList))
    print(min(sumList))

solution()