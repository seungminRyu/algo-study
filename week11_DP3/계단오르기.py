def solution():
    n = int(input())
    stair = [int(input()) for _ in range(n)]
    dp = [0 for _ in range(n)]
    
    for i in range(n):
        if i == 0:
            dp[0] = stair[0]
        elif i == 1:
            dp[1] = max(stair[0] + stair[1], stair[1])
        elif i == 2:
            dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
        else:
            dp[i] = max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i])

    print(dp[-1])

solution()