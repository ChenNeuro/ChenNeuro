turn = 0
while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    turn += 1
    pos = []
    for i in range(n):
        a, b = map(int, input().split())
        if d >= b:
            pos.append([float(a-(d**2-b**2)**0.5),float(a+(d**2-b**2)**0.5)])
    input()
    if len(pos) < n:
        print(f'Case {turn}: -1')
    else:
        pos.sort(reverse=True)
        number = len(pos)
        c = pos[0][0]
        for j in range(1,n):
            if c > pos[j][1]:
                c = pos[j][0]
            else:
                number -= 1
        print(f'Case {turn}: {number}')
