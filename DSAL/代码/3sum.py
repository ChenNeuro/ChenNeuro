def threesum(nums):
    nums.sort()
    n = len(nums)
    res = 0
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i + 1, n - 1
        while l < r and nums[i] <= 0:
            if nums[i] + nums[l] + nums[r] > 0:
                r -= 1
                while nums[r+1] == nums[r]:
                    r -= 1
            elif nums[i] + nums[l] + nums[r] < 0:
                l += 1
                while nums[l-1] == nums[l]:
                    l += 1
            else:
                res += 1
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1] and l < n-1:
                    l += 1
                while l < r and nums[r] == nums[r+1] and r >= 0:
                    r -= 1
    return res


ans = threesum(list(map(int, input().split())))
print(ans)
