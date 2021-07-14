def solution():
    n = int(input())
    dp = [0 for _ in range(n)]

    dp[0] = 1
    dp[1] = 2
    
    for i in range(2, n):
        x = dp[i-1] + dp[i-2]
        dp[i] = x % 1000000007

    print(dp[n-1])

solution()