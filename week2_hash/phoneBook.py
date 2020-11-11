def solution(phone_book):
    numList = phone_book
    numHash = {}
    answer = True

    numList.sort(key=len)
    numList.reverse
    minLen = len(numList[0])
    
    for num in numList:
        numLen = len(num)
        if (numLen in numHash):
            numHash[numLen].append(num)
        else:
            numHash[numLen] = []
            numHash[numLen].append(num)

    keyList = list(numHash.keys())

    for num in numList:
        numLen = len(num)
        i = numLen
        while(i <= 20):
            if(i in numHash):
                for otherNum in numHash[i]:
                    if (otherNum.startswith(num) & (otherNum != num)):
                        x = False
                    else:
                        x = True
                    answer &= x
                    print(num, otherNum, x)
            i += 1
    
    print(answer)

testcase = ["119", "97674223", "1195524421"]
solution(testcase)