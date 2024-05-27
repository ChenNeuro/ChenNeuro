def min_setup_time(sticks):
    n = len(sticks)
    check = [0] * n
    setup_time = 0
    while (0 in check):
        i = 0
        for j in range(n):
            if check[j] == 0:
                i = j
                break
        current = sticks[i]
        check[i] = 1
        setup_time += 1
        i += 1
        while i < n:

            if check[i] == 0 and current[0] <= sticks[i][0] and current[1] <= sticks[i][1]:
                check[i] = 1
                current = sticks[i]
            i += 1

    return setup_time


T = int(input())
for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    sticks = [(data[i], data[i + 1]) for i in range(0, 2 * n, 2)]
    sticks.sort()
    print(min_setup_time(sticks))