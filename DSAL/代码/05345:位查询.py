"""
N, M = map(int, input().split())
nlist = list(map(int, input().split()))

for i in range(M):
    opt, num = input().split()
    num = int(num)
    if opt == "Q":
        tmp = 0
        for j in nlist:
            if (j >> num) & 1:
                tmp += 1
        print(tmp)
    else:
        for j in range(N):
            nlist[j] = (nlist[j] + num) % 65536
"""

s = []
add = 0
for i in range(16):
    s.append([0]*(2 ** (i + 1)))
n, m = map(int, input().split())
num = list(map(int, input().split()))
for i in range(n):
    for j in range(16):
        s[j][num[i] % (2 ** (j + 1))] += 1
for j in range(16):
    for k in range(1, 2 ** (j + 1)):
        s[j][k] += s[j][k - 1]
for i in range(m):
    st = input().split()
    if st[0] == 'C':
        add += int(st[1])
        add %= 65536
    else:
        ind = int(st[1])
        al = 2 ** (ind + 1)
        x = -(add % al) + al // 2 - 1
        y = x + al // 2
        ans = 0
        if x < 0:
            x += al
            ans = n
        print(ans + s[ind][y] - s[ind][x])
