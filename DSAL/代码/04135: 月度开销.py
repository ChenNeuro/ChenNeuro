n, m = map(int, input().split())
expenditure = []
for _ in range(n):
    expenditure.append(int(input()))


def check(x):
    num, s = 1, 0
    for i in range(n):
        if s + expenditure[i] > x:
            s = expenditure[i]  # 装不了了
            num += 1  # 新开一个月
        else:
            s += expenditure[i]  # 向月里加天

    return [False, True][num > m]


lo = max(expenditure)
hi = sum(expenditure) + 1  # 绝对大值
ans = 1
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):  # 返回True，是因为num>m，是确定不合适
        lo = mid + 1  # 所以lo可以置为 mid + 1。
    else:
        ans = mid  # 如果num==m, mid就是答案
        hi = mid

# print(lo)
print(ans)