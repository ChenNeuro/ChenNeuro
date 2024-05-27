from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))

window = deque()
stack = deque()

for i in range(n):
    # Remove elements that are out of the window from the left of the deque
    if window and window[0] == i - k:
        window.popleft()

    # Remove elements that are smaller than the current element from the right of the deque
    while window and nums[window[-1]] < nums[i]:
        window.pop()

    window.append(i)

    # The maximum element in the window is at the left of the deque
    if i >= k - 1:
        stack.append(nums[window[0]])

print(*stack)