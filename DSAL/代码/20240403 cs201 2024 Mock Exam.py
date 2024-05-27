"""
arr = list(map(str,input().split()))
print(*arr[::-1])
"""

"""
from collections import deque

M, N = map(int, input().split())
words = list(map(int, input().split()))

memory = deque()
lookup_count = 0

for word in words:
    if word not in memory:
        lookup_count += 1
        if len(memory) == M:
            memory.popleft()
        memory.append(word)

print(lookup_count)
"""

"""
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

if k == 0:
    if arr[0] > 1:
        print(1)
    else:
        print(-1)
elif k == n or arr[k-1] < arr[k]:
    print(arr[k-1])
else:
    print(-1)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(s):
    if len(s) == 1:
        return TreeNode(s)
    mid = len(s) // 2
    left = build_tree(s[:mid])
    right = build_tree(s[mid:])
    return TreeNode('0', left, right)

def postorder_traversal(root):
    if root is None:
        return ''
    left = postorder_traversal(root.left)
    right = postorder_traversal(root.right)
    if root.val == '0':
        if left == 'B' and right == 'B':
            root.val = 'B'
        elif left == 'I' and right == 'I':
            root.val = 'I'
        else:
            root.val = 'F'
    return left + right + root.val

def main():
    N = int(input())
    s = input().strip()
    root = build_tree(s)
    print(postorder_traversal(root))

main()
