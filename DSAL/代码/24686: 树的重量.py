k, n = [int(x) for x in input().split()]
f, g, dep = [], [], []
tot = (1 << k) - 1
for _ in range(tot+1):
    f.append(0)
    g.append(0)
    dep.append(0)
for i in range(tot, 0, -1):
    dep[i] = 1 if i * 2 > tot else dep[i * 2] + 1
for _ in range(n):
    a = [int(x) for x in input().split()]
    if len(a) == 2:
        u = a[1]
        s = f[1]
        while u != 1:
            s += f[u]
            u >>= 1
        ans = s * ((1 << dep[a[1]]) - 1) + g[a[1]]
        print(ans)
    elif len(a) == 3:
        u = a[1]
        w = a[2] * ((1 << dep[u]) - 1)
        f[u] += a[2]
        while u != 1:
            u >>= 1
            g[u] += w