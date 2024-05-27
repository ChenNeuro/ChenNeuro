stuffNum, Space = map(int,input().split())
occupy = [0] + list(map(int,input().split()))
Space_all = sum(occupy)
if Space_all < Space:
    print(0)
else:
    dp = [0 for j in range(Space_all+1-Space)]
    for i in range(1, stuffNum+1):
        for j in range(Space_all-Space,occupy[i]-1,-1):
            if j >= occupy[i]:
                dp[j] = max(dp[j], dp[j-occupy[i]]+occupy[i])
    print(Space_all - dp[Space_all-Space])
