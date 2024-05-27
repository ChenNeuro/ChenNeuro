from collections import deque
M, N = map(int, input().split())
arr = list(map(int, input().split()))
window = deque()
ans = 0
for i in arr:
    if i in window:
        continue
    else:
        ans += 1
        if len(window) == M:
            window.popleft()
        window.append(i)
print(ans)