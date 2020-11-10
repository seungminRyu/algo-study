inputLs = list( map(lambda x: int(x), input().split() ))

typeNum = inputLs[0]
amount = inputLs[1]
coinType = []
divCnt = 0

for i in range(typeNum):
    coinType.append( int(input()) )

for i in range(typeNum, 0, -1):
    while (amount >= coinType[i-1]):
        amount = amount - coinType[i-1]
        divCnt += 1
        
print(divCnt)
