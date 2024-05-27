n, a, b = map(int, input().split())
plants = list(map(int, input().split()))
ans = 0
ta = a
tb = b
while plants:
    if len(plants) == 1:
        if plants[0] <= max(ta,tb):
            print(ans)
        else:
            print(ans + 1)
        exit()
    lp = plants.pop(0)
    if ta < lp:
        ans += 1
        ta = a - lp
    else:
        ta -= lp
    rp = plants.pop()
    if tb < rp:
        ans += 1
        tb = b - rp
    else:
        tb -= rp
print(ans)
