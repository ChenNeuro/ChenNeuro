n = int(input())
dp = [[] for i in range(n)]
for i in range(n):
    dp[i] = list(map(int, input().split()))


def solve(dp):
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])
    return dp[0][0]

print(solve(dp))
