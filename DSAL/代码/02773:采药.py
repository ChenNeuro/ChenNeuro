T, M = map(int, input().split())
cost = []
w = []
for i in range(M):
    ct, wt =map(int, input().split())
    cost.append(ct)
    w.append(wt)

dp = [[0 for j in range(T+1)] for i in range(M+1)]

for i in range(1, M+1):
    for j in range(1, T+1):
        if j < cost[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]]+w[i-1])
print(dp[M][T])
