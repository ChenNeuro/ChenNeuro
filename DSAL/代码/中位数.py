from bisect import bisect_left
a, b, cnt, now = [], [], 0, 0
for i in range(int(input())):
    opt = input().split()
    if opt[0] == 'add':
        v = int(opt[1])
        a.insert(bisect_left(a,[v, 0]), [v, cnt])
        b.append(v)
        cnt += 1
    elif opt[0] == "query":
        l = len(a)
        if l & 1:
            print(a[l >> 1][0])
        else:
            ans = (a[l >> 1][0] + a[l - 1 >> 1][0]) / 2
            print(ans if int(ans) != ans else int(ans))
    else:
        v = b[now]
        now += 1
        a.pop(bisect_left(a,[v, 0]))
