# 基于 23 工学院 苏王捷
import heapq

num1 = 1
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    print(f"Board #{num1}:")
    matrix = [[" "] * (w + 2)] + [[" "] + list(input()) + [" "] for _ in range(h)] + [[" "] * (w + 2)]
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num2 = 1
    while True:
        x1, y1, x2, y2 = map(int, input().split())
        if x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0:
            break
        queue, flag = [], False
        vis = set()
        heapq.heappush(queue, (0, x1, y1, -1))   ##初始情况-1下，线段数+1，i代表方向
        matrix[y2][x2] = " "
        vis.add((-1, x1, y1))
        while queue:
            step, x, y, dirs = heapq.heappop(queue)
            if x == x2 and y == y2:
                flag = True
                break
            for i, (dx, dy) in enumerate(dir):
                px, py = x + dx, y + dy
                if 0 <= px <= w + 1 and 0 <= py <= h + 1 and (i, px, py) not in vis and matrix[py][px] != "X":
                    vis.add((i, px, py))
                    heapq.heappush(queue, (step + (dirs != i), px, py, i))
        if flag:
            print(f"Pair {num2}: {step} segments.")
        else:
            print(f"Pair {num2}: impossible.")
        matrix[y2][x2] = "X"
        num2 += 1
    print()
    num1 += 1
