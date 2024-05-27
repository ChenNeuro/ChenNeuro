def find(nums):
    if len(nums) == 1:
        return abs(nums[0] - 42) <= 0.000001
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            a = nums[i]
            b = nums[j]
            remaining_nums = []
            for k in range(len(nums)):
                if k != i and k != j:
                    remaining_nums.append(nums[k])
            if find(remaining_nums + [a+b]) or find(remaining_nums + [a*b]):
                return True
            if find(remaining_nums + [a-b]) and a > b:
                return True
            if find(remaining_nums + [b-a]) and b > a:
                return True
            if a != 0 and find(remaining_nums + [b/a]):
                return True
            if b != 0 and find(remaining_nums + [a/b]):
                return True
    return False


n = int(input())
card = [int(i) for i in input().split()]
print("YES" if find(card) else "NO")