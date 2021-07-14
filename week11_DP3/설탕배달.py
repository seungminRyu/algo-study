def solution():
    n = int(input())
    cnt = 0

    if(n==7 or n==4 or n==2 or n==1): 
        print(-1)
        return

    while (1):
        if(n <= 12):
            break
        n -= 5
        cnt += 1
    
    if (n % 3 == 0):
        cnt += n // 3
    elif (n % 5 == 0):
        cnt += n // 5
    else:
        n -= 5
        cnt += 1
        if (n % 3 == 0):
            cnt += n // 3
    
    print(cnt)

solution()