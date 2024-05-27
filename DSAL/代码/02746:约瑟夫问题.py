while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    stack = [_ for _ in range(1, n + 1)]
    i = 1
    while len(stack) != 1:
        # print(stack)
        if i == m:
            stack.pop(0)
            i = 1
        else:
            stack.append(stack.pop(0))
            i += 1
    print(*stack)
