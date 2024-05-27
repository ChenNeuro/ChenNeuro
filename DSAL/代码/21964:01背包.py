items, space = map(int, input().split())
weight_value = [tuple(map(int, input().split())) for _ in range(items)]
dp = [0 for j in range(space+1)]

for i in range(items):
    for j in range(space, weight_value[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j-weight_value[i][0]] + weight_value[i][1])
print(dp[space])