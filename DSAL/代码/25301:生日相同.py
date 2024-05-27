dic = dict()
ans = []
for i in range(int(input())):
    num, month, day = map(str, input().split())
    if (month, day) in dic.keys():
        dic[(month, day)].append(num)
    else:
        dic[(month, day)] = [num]
for (month, day), nums in dic.items():
    if len(nums) > 1:
        ans.append((month, day, *nums))
ans.sort(key=lambda x:(int(x[0]),int(x[1])))
for i in ans:
    print(*i)

