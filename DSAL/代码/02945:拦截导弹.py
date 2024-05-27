N = int(input())
nums = list(map(int, input().split()))  # 输入一组序列
length = len(nums)
# print(n)

dp = [1] * (length + 1)

for i in range(length):
    for j in range(0, i):
        if nums[i] <= nums[j]:
            # 状态：dp[i] 表示以 nums[i] 结尾的「上升子序列」的长度
            # 当nums[i]前面存在小于nums[i]的nums[j],
            # 则暂存在dp[j]+1就是当前nums[i]的最长增长子序列的长度
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))  # 用函数max直接找到dp数组的最大值，无需再遍历了