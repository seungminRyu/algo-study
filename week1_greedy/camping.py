def count(a):
    availableDay = a[0]
    dayInRow = a[1]
    holiday = a[2]
    usedDay = int(holiday / dayInRow) * availableDay

    if (holiday % dayInRow > 0):
        usedDay += holiday % dayInRow;

    return usedDay

def main():
    caseCnt = 0
    caseLs = []

    while(1):
        a = list( map(lambda x: int(x), input().split() ))

        if (a[0] == 0 and a[1] == 0 and a[2] == 0):
            break
        else:
            caseLs.append(a)
            caseCnt += 1

    for i in range(caseCnt):
        print(f"Case {i+1}: {count(caseLs[i])}")

main()