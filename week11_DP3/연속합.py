def solution():
    n = int(input())
    dp = list(map(int, input().split(" ")))
    maxSum = dp[0]

    for i in range(1, n):
        if dp[i-1] > 0 and dp[i] + dp[i-1] > 0:
            dp[i] += dp[i-1]
        if maxSum < dp[i]:
            maxSum = dp[i]
    
    print(maxSum)

solution()