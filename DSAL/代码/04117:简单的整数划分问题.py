def partition_number(N):
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-i]
    return dp[N][N]

while True:
    try:
        print(partition_number(int(input())))  # Output: 7
    except EOFError:
        break