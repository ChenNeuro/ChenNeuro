from collections import deque
for i in range(int(input())):
    a = deque()
    b = []
    tag = True
    for j in range(int(input())):
        opt = list(map(str, input().split()))
        if opt[0] == "push" and tag:
            a.append(int(opt[1]))
            b.append(int(opt[1]))
        elif opt[0] == "pop" and tag:
            if len(a) == 0:
                tag = False
            if tag:
                a.popleft()
                b.pop()
    if tag:
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))
    else:
        print("error")
        print("error")
