def solution(prices):
    answer = []

    for i in prices:
        if (i+1 < len(prices)):
            riseCnt = 1
            k = i
            while(((prices[k+1]-prices[k]) > 0) & (k+2 < len(prices))):
                riseCnt += 1
                k += 1
            answer.append(riseCnt+1)
        else:
            answer.append(0)

    print(answer)

testcase = [1, 2, 3, 2, 3]

solution(testcase)