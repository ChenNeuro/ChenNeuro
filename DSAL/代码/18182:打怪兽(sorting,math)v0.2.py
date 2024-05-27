nCases = int(input())
for i in range(nCases):
    n, m, b = map(int, input().split())
    skills = []
    for j in range(n):
        ti, xi = map(int, input().split())
        skills.append((ti, xi))
    skills.sort(key=lambda x: (-x[0], x[1]))
    time = 1
    tm = m
    while skills and b > 0:
        ti, xi = skills.pop()
        if ti == time and tm > 0:
            b -= xi
            tm -= 1
        if ti > time:
            time = ti
            tm = m
            skills.append((ti, xi))
        if b <= 0:
            print(time)
            break
    if b > 0:
        print('alive')
