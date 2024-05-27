t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    nlist = list(map(int, input().split()))
    non = []
    for i in nlist:
        if i % x:
            non.append(i)
    if sum(nlist) % x != 0:
        print(n)
    else:
        if non:
            print(n - 1)
        else:
            print(-1)