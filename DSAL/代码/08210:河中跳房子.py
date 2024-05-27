L, n, m = map(int, input().split())
rock = [0]
for i in range(n):
    rock.append(int(input()))
rock.append(L)


def check(x):
    num = 0
    now = 0
    for i in range(1, n + 2):
        if rock[i] - now < x:  # 可去石头+1
            num += 1
        else:
            now = rock[i]  # 下一个石头

    return [False, True][num > m]


# lo, hi = 起点, 终点
lo, hi = 0, L + 1
ans = -1
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:  # 返回False，有可能是num==m
        ans = mid  # 如果num==m, mid就是答案
        lo = mid + 1

# print(lo-1)
print(ans)