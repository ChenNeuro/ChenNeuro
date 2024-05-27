import math
while True:
    n = int(input())
    if n == 0:
        break

    ans = 0
    f = True
    for _ in range(n):
        v, t = map(int, input().split())
        if t < 0:
            continue
        if f:
            ans = (4.5/v) * 3600 + t
            f = False
        tmp = (4.5/v) * 3600 + t
        ans = min(ans,tmp)
    print(math.ceil(ans))