def solution():
    n = input()
    lng = len(n)

    nReversed = []
    for i in range(lng -1, 0 -1, -1):
        nReversed.append(int(n[i]))
    
    print(nReversed)

solution()

