from collections import deque
for _ in range(int(input())):
    line = deque()
    for i in range(int(input())):
        opt1, opt2 = map(int, input().split())
        if opt1 == 1:
            line.append(opt2)
        elif opt2 == 0:
            line.popleft()
        else:
            line.pop()
    if line:
        print(' '.join(map(str, line)))
    else:
        print("NULL")