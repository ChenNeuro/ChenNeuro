import itertools
import queue
while True:
    pos = []
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        exit()
    line = queue.Queue()
    line.put(n*3)
    line.put(n//2)
    ans = 0
    for i in range(24):
        length = line.qsize()
        for j in range(length):
            cur = line.get()
            if cur == m:
                ans = i
                break
            line.put(cur*3)
            line.put(cur//2)
        if ans:
            break
    ans += 1
    print(ans)
    for i in itertools.product("HO", repeat=ans):
        possible = ("".join(i))
        cur_pos = n
        for j in possible:
            if j == "H":
                cur_pos *= 3
            else:
                cur_pos //= 2
        if cur_pos == m:
            print(possible)
            break
