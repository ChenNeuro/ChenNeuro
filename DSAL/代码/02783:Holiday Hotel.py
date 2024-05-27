while True:
    N = int(input())
    ans = 1
    if N == 0:
        break
    D_C = []
    for i in range(N):
        d, c = map(int, input().split())
        D_C.append((d, c))
    D_C.sort(key=lambda x: (x[0],x[1]))
    # print(D_C)
    minium = D_C[0][1]
    for i in range(1,N):
        if D_C[i][1] >= minium:
            continue
        if D_C[i][1] < minium:
            minium = D_C[i][1]
            ans += 1
    print(ans)


