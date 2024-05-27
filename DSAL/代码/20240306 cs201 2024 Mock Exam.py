"""
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
"""


"""
numDisks, a, b, c = input().split()
numDisks = int(numDisks)

def moveOne(x, init, desti):
    print(f"{x}:{init}->{desti}")
    return


def move(numDisks, init, temp, desti):
    if numDisks == 1:
        moveOne(1, init, desti)
    else:
        move(numDisks - 1, init, desti, temp)
        moveOne(numDisks, init, desti)
        move(numDisks - 1, temp, init, desti)

move(numDisks, a, b, c)
"""


"""
from collections import deque
while True:
    n, p, m = map(int, input().split())
    if n == 0 and p == 0 and m == 0:
        break
    queue = deque(i for i in range(1, n + 1))
    for i in range(p-1):
        queue.append(queue.popleft())
    ans = []
    i = 0

    while len(queue) != 1:
        i += 1
        x = queue.popleft()
        if i == m:
            i = 0
            ans.append(x)
            continue
        else:
            queue.append(x)

    ans.append(queue.popleft())
    print(",".join(str(_) for _ in ans))
"""


"""
n = int(input())
task_time = list(map(int, input().split()))
for i in range(n):
    task_time[i] = (task_time[i], i + 1)


def minimumWaitingTime(queries):
    ans = []
    queries = sorted(queries)
    total_waiting_time = 0
    for index, time_cost_index in enumerate(queries):
        # print(f"index: {index} time_cost: {time_cost}")
        queries_Left = len(queries)-(index+1)
        total_waiting_time += time_cost_index[0] * queries_Left
        ans.append(time_cost_index[1])
    print(*ans)
    print("%.2f" % (total_waiting_time/n))

minimumWaitingTime(task_time)

"""


"""
n = int(input())
x_y = [tuple(map(int, i[1:-1].split(","))) for i in input().split()]
# print(type(x_y))
cost = list(map(int, input().split()))
sorted_cost = sorted(cost)
ptov = []

house = []
for i in range(n):
    x, y = x_y[i][0], x_y[i][1]
    p2v = (x+y)/cost[i]
    house.append((p2v, cost[i]))
    ptov.append(p2v)

sorted_ptov = sorted(ptov)

if n % 2 == 0:
    mid_cost = sorted_cost[len(sorted_cost)//2] + sorted_cost[len(sorted_cost)//2 - 1]
    mid_cost /= 2
    mid_p2v = sorted_ptov[len(sorted_ptov)//2] + sorted_ptov[len(sorted_ptov)//2 - 1]
    mid_p2v /= 2
else:
    mid_cost = sorted_cost[len(sorted_cost)//2]
    mid_p2v = sorted_ptov[len(sorted_ptov)//2]
ans = 0
for i in house:
    if mid_cost > i[1] and mid_p2v < i[0]:
        ans += 1
print(ans)
# print(x_y)
"""


n = int(input())
dic = dict()
for i in range(n):
    name, params = input().split("-")
    x = float(params[:-1])
    x = int(x) if x.is_integer() else float(x)
    if name in dic.keys():
        if params[-1] == "M":
            dic[name][0].append(x)
        else:
            dic[name][1].append(x)
    else:
        if params[-1] == "M":
            dic[name] = [[x], []]
        else:
            dic[name] = [[], [x]]

ans_l = []
for name, params in dic.items():
    params[0].sort()
    params[1].sort()
    # print(params)
    ans = f"{name}: "
    tmp = []
    for m in params[0]:
        tmp.append(str(m) + "M")
    for b in params[1]:
        tmp.append(str(b) + "B")
    ans += ", ".join(tmp)
    ans_l.append(ans)
ans_l.sort()
for i in ans_l:
    print(i)
