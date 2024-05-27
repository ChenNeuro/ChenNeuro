while True:
    try:
        X, Y = input().split()
        a = len(X)
        b = len(Y)
        dp = [[0 for j in range(b+1)] for i in range(a+1)]
        for i in range(1, a+1):  # 1-a的自然数列表
            for j in range(1, b+1):
                if X[i-1] == Y[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1  # 这是递进程序
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 这是回溯程序
        print(dp[a][b])
    except EOFError:
        break
